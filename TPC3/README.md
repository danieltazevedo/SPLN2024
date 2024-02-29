Automatic toml file generator.

The project name field is obtained with the glob module, which collects the list of all .py files and the first one from that list is chosen.

The name and email fields are obtained through the METADATA.json file found in the system home page.

Finally, the .toml file is generated with the previous information.
