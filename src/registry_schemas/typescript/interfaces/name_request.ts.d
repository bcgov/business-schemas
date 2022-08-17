/* tslint:disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export type TheLegalTypeOfTheBusiness =
  | "A"
  | "B"
  | "BC"
  | "BEN"
  | "C"
  | "CC"
  | "CCC"
  | "CEM"
  | "CP"
  | "CS"
  | "CUL"
  | "EPR"
  | "FI"
  | "FOR"
  | "GP"
  | "LIC"
  | "LIB"
  | "LL"
  | "LLC"
  | "LP"
  | "MF"
  | "PA"
  | "PAR"
  | "PFS"
  | "QA"
  | "QB"
  | "QC"
  | "QD"
  | "QE"
  | "REG"
  | "RLY"
  | "S"
  | "SB"
  | "SP"
  | "T"
  | "TMY"
  | "ULC"
  | "UQA"
  | "UQB"
  | "UQC"
  | "UQD"
  | "UQE"
  | "XCP"
  | "XL"
  | "XP"
  | "XS";
export type TheTypeOfNameRequest = string;

export interface NameRequestSchema {
  nrNumber?: string;
  legalName?: string;
  legalType: TheLegalTypeOfTheBusiness;
  requestType?: TheTypeOfNameRequest;
  status?: string;
  expires?: string;
  consent?: string;
  submittedBy?: string;
  address?: TheAddressSchema;
  [k: string]: unknown;
}
export interface TheAddressSchema {
  streetAddress: string;
  streetAddressAdditional?: string;
  addressCity: string;
  addressCountry: string;
  addressRegion: string | null;
  postalCode: string;
  deliveryInstructions?: string | null;
  [k: string]: unknown;
}