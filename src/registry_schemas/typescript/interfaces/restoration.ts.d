/* tslint:disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export type TheTypeOfRestorationSuchAsFullRestorationLimitedRestorationEtc = "fullRestoration" | "limitedRestoration";
export type TheDateTheLimitedRestorationIsEnds = string;

export interface Restoration {
  restoration: {
    date: string;
    type: TheTypeOfRestorationSuchAsFullRestorationLimitedRestorationEtc;
    expiry?: TheDateTheLimitedRestorationIsEnds;
    [k: string]: unknown;
  };
  [k: string]: unknown;
}