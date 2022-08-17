import { compileFromFile } from "json-schema-to-typescript";
import axios from "axios";
import * as fs from "fs";
import { globby } from "globby";

const paths = await globby("../../schemas/*.json");
const fileResolver = {
  async read(file: any) {
    // console.debug(`Resolve File: ${file.url}`);
    return fs.readFileSync(file.url);
  },
};

const httpResolver = {
  async read(file: any) {
    const camelToSnakeCase = (str: string) => str.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);
    const bcrsUrl = "https://bcrs.gov.bc.ca/.well_known/schemas/";
    const githubUrl = "https://raw.githubusercontent.com/bcgov/business-schemas/main/src/registry_schemas/schemas/";
    let target_url = camelToSnakeCase(file.url.replace(bcrsUrl, githubUrl) + ".json");
    target_url = target_url.replace('parties', 'party')
    // console.debug(`Resolve URL: ${target_url}`);
    let response = await axios.get(target_url);
    if (response.data) {
      return response.data;
    } else {
      throw new Error("No data!");
    }
  },
};

// TODO add version to the text of each file using one of the options.
paths.forEach(async (path: string) => {
  console.log(`Generating file: ${path}`)
  const result = await compileFromFile(path, {
    $refOptions: {
      resolve: {
        external: true,
        file: fileResolver,
        http: httpResolver,
      }
    },
  });
  const outputFile = path.replace(/^.*[\\\/]/, "").replace('json', 'ts.d');
  await fs.writeFileSync(`../interfaces/${outputFile}`, result);
});
