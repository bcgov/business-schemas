/* tslint:disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export type DifferencesFiledInTheCorrection = DifferencesFiledInTheCorrection1 & DifferencesFiledInTheCorrection2;
export type DifferencesFiledInTheCorrection1 = {
  [k: string]: unknown;
};
export type PathOfThePropertyInJson = string;

export interface DifferencesFiledInTheCorrection2 {
  diff?: {
    oldValue: OriginalValue;
    newValue: CorrectedValue;
    path: PathOfThePropertyInJson;
    [k: string]: unknown;
  }[];
  [k: string]: unknown;
}
export interface OriginalValue {
  [k: string]: unknown;
}
export interface CorrectedValue {
  [k: string]: unknown;
}