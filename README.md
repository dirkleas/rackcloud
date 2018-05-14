# rackcloud
Cloud services for [rackcli](https://github.com/dirkleas/rackcli), please review
for rationale and use cases (e.g. how to make your
[VCV Rack](https://github.com/VCVRack/Rack) workflow even more awesome!).

In the short term, the principal service will include the following REST service(s):

1. catalog/share - share your complete `catalog.json` generated via my [VCV Rack fork](https://github.com/dirkleas/Rack) (not a `catalog.partial.json` generated
from my [DLwigglz r4xHrx](https://github.com/dirkleas/DLwigglz))

Many more services will be coming soon, focusing on community sourced metadata,
documentation, tutorials, etc..

**Example Usage**

Details pending service deployment on our cloud provider.

```
curl -d "@catalog.json" -X POST http://SERVICE:PORT/catalog/share
```

Again, check out the open issues marked "enhancement" for additional active conversations and please submit your own features/priorities/suggestions [there](https://github.com/dirkleas/rackcli/issues) as well. You can also reach out via the official [VCV Rack group](https://www.facebook.com/groups/vcvrack/) on Facebook or [message](https://www.facebook.com/dirkleas) me directly -- front there, we can bounce out to Skype or email as appropriate.

--

**Licenses**

All concepts and source code in this repository is licensed under [BSD-3-Clause](LICENSE) by Dirk Leas.
