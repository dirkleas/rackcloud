# rackcloud
Cloud services for [rackcli](https://github.com/dirkleas/rackcli) (please review
for rationale and use cases -- how to make your
[VCV Rack](https://github.com/VCVRack/Rack) workflow even more awesome!).

There are two initial services to help with the care and feeding of your
`catalog.json` if you prefer to not run my [fork](https://github.com/dirkleas/Rack)
renders a complete catalog with width data:

1. sync - submit a list of your plugin modules from `catalog.partial.json` generated
from [DLwigglz r4xHrx](https://github.com/dirkleas/DLwigglz) and get back the
missing widths to generate a full `catalog.json` with the crowd-sourced "master"
version in the cloud
1. share - share your [fork](https://github.com/dirkleas/Rack) catalog widths
from the generated `catalog.json` using the **File.Catalog** menu option so others can have width-enhanced catalogs. You
can even share `patch.json` widths generated via
[DLwigglz r4xH4x](https://github.com/dirkleas/DLwigglz) `patch` button to send smaller width
pools -- *this would be handy for plugin developers!*

These cloud services were designed for use with [rackcli](https://github.com/dirkleas/rackcli) catalog services. Refer to the
**Example Usage -- Live Features** there background and usage.

Many more services will be coming soon, focusing on community sourced metadata,
documentation, tutorials, etc..

Again, check out the open issues marked "enhancement" for additional active conversations and please submit your own features/priorities/suggestions [there](https://github.com/dirkleas/rackcli/issues) as well. You can also reach out via the official [VCV Rack group](https://www.facebook.com/groups/vcvrack/) on Facebook or [message](https://www.facebook.com/dirkleas) me directly -- front there, we can bounce out to Skype or email as appropriate.

--

**Licenses**

All concepts and source code in this repository is licensed under [BSD-3-Clause](LICENSE) by Dirk Leas.
