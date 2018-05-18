# -*- coding: utf-8 -*-

import json, boto3
from hashlib import sha256

def hash(rv, ps, pv, ms):
    'hash rack version, plugin slug/version, model slug'
    return(sha256(str.encode('{}|{}|{}|{}'.format(rv, ps, pv, ms))).hexdigest())

def vet_share_corpus(c):
    'verify and return valid and invalid corpus request, len(key)==64 and is_corpus_tuple(value)'
    def is_valid(v): return(len(v) == 5 and isinstance(v[0], str) and isinstance(v[1], str) and
                            isinstance(v[2], str) and isinstance(v[3], str) and isinstance(v[4], int))
    return({k:v for k,v in c.items() if len(k) == 64 and is_valid(v)},
           {k:v for k,v in c.items() if not len(k) == 64 or not is_valid(v)})

def cloud_share(request, corpus):
    'merge request into corpus returning updated corpus and errors, add crowd validation, deploy serverless'
    request, errors = vet_share_corpus(request)
    {k:v for k, v in request.items() if k in corpus.keys()} # only add new plugin modules
    return({**corpus, **request}, errors)

def share(event, context):
    'share local corpus'
    request = json.loads(event['body'])
    obj = boto3.resource('s3').Object('rackcloud', 'corpus.json')
    corpus = json.loads(obj.get()['Body'].read().decode('utf-8')) # load corpus
    request, unknowns = vet_share_corpus(request)
    corpus = cloud_share(request, corpus)
    obj.put(Body=str.encode(json.dumps(corpus[0]))) # save updated corpus
    body = {
        "message": "share completed, review corpus and unknowns",
        "corpus": corpus,
        "unknowns": unknowns
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def vet_sync_corpus(request):
    return(all(isinstance(hash, str) and len(hash) == 64 for hash in request))

def cloud_sync(request, corpus):
    'request projected corpus and uknowns, deploy serverless'
    if not vet_sync_corpus(request): return({}, request)
    return(({k:v for k, v in corpus.items() if k in request},
           [r for r in request if not r in corpus.keys()]))

def sync(event, context):
    'sync corpus based on local request (hashs)'
    request = json.loads(event['body'])
    obj = boto3.resource('s3').Object('rackcloud', 'corpus.json')
    corpus = json.loads(obj.get()['Body'].read().decode('utf-8')) # load corpus
    corpus, unknowns = cloud_sync(request, corpus)
    body = {
        "message": "sync completed, review corpus and unknowns",
        "corpus": corpus,
        "unknowns": unknowns
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
