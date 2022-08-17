Run generate_typescript to generate the interfaces.
Right now it seems json-schema-to-typescript is relying on json-schema-ref-parser - which seems to have an issue with resolving some of our references. 
This will be in draft state until that's fixed.