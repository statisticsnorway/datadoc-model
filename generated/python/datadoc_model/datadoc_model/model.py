# generated by datamodel-codegen:
#   filename:  metadata-container-json-schema.json
#   timestamp: 2024-07-08T12:35:21+00:00

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, Field, RootModel

from datadoc_model.datadoc_base_model import DatadocBaseModel


class Assessment(str, Enum):
    SENSITIVE = "SENSITIVE"
    PROTECTED = "PROTECTED"
    OPEN = "OPEN"


class DataSetStatus(str, Enum):
    DRAFT = "DRAFT"
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    DEPRECATED = "DEPRECATED"


class DataSetState(str, Enum):
    SOURCE_DATA = "SOURCE_DATA"
    INPUT_DATA = "INPUT_DATA"
    PROCESSED_DATA = "PROCESSED_DATA"
    STATISTICS = "STATISTICS"
    OUTPUT_DATA = "OUTPUT_DATA"


class UseRestriction(str, Enum):
    DELETION_ANONYMIZATION = "DELETION_ANONYMIZATION"
    PROCESS_LIMITATIONS = "PROCESS_LIMITATIONS"
    SECONDARY_USE_RESTRICTIONS = "SECONDARY_USE_RESTRICTIONS"


class CustomTypeForDatasetMetadatum(DatadocBaseModel):
    key: Optional[str] = Field(None, description="Custom type KEY", title="Key")
    value: Optional[Union[str, list, dict[str, Any]]] = Field(
        None,
        description="Custom type VALUE (of type string, array or object).",
        title="Value",
    )


class DataType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    DATETIME = "DATETIME"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    ARRAY = "ARRAY"


class VariableRole(str, Enum):
    IDENTIFIER = "IDENTIFIER"
    MEASURE = "MEASURE"
    START_TIME = "START_TIME"
    STOP_TIME = "STOP_TIME"
    ATTRIBUTE = "ATTRIBUTE"


class IsPersonalData(str, Enum):
    NOT_PERSONAL_DATA = "NOT_PERSONAL_DATA"
    PSEUDONYMISED_ENCRYPTED_PERSONAL_DATA = "PSEUDONYMISED_ENCRYPTED_PERSONAL_DATA"
    NON_PSEUDONYMISED_ENCRYPTED_PERSONAL_DATA = (
        "NON_PSEUDONYMISED_ENCRYPTED_PERSONAL_DATA"
    )


class SentinelValues(DatadocBaseModel):
    sentinel_value_uri: Optional[AnyUrl] = Field(
        None,
        description="A link (URI) to a standardized list of sentinel values included in the variable, eg. a link to a codelist in Klass (https://www.ssb.no/en/klass/)",
        title="Sentinel value URI",
    )
    sentinel_value_elements: Optional[list[str]] = Field(
        None,
        description="A selection (subset) of sentinel values in the 'sentinel_value_uri' \u200b\u200bapplicable to the data set.",
        title="Sentinel value elements",
    )


class CustomTypeForVariableMetadatum(DatadocBaseModel):
    key: Optional[str] = Field(None, description="Custom type KEY", title="Key")
    value: Optional[Union[str, list, dict[str, Any]]] = Field(
        None,
        description="Custom type VALUE (of type string, array or object).",
        title="Value",
    )


class LanguageStringTypeItem(DatadocBaseModel):
    languageCode: Optional[str] = Field(
        None, description="Language code (ISO 639-1)", title="Language code"
    )
    languageText: Optional[str] = Field(
        None, description="Language text", title="Language text"
    )


class LanguageStringType(RootModel[Optional[list[LanguageStringTypeItem]]]):
    root: Optional[list[LanguageStringTypeItem]] = None


class TemporalityTypeType(str, Enum):
    FIXED = "FIXED"
    STATUS = "STATUS"
    ACCUMULATED = "ACCUMULATED"
    EVENT = "EVENT"


class PseudoDataset(DatadocBaseModel):
    dataset_pseudo_time: Optional[AwareDatetime] = Field(
        None,
        description="Time at which the dataset was pseudonymized. In ISO 8601 format.",
        title="Dataset pseudo time",
    )
    source_dataset_path: Optional[str] = Field(
        None,
        description="Path to the unpseudonymized dataset. Specified as a file path, URL or URI.",
        title="Source dataset path",
    )


class SourceVariableDataType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    DATETIME = "DATETIME"


class PseudoVariable(DatadocBaseModel):
    short_name: Optional[str] = Field(
        None,
        description="Physical name of the variable in the dataset. Should match the recommended short name.",
        title="Short name",
    )
    data_element_path: Optional[str] = Field(
        None,
        description="Path to a single, concrete data element in the dataset.",
        title="Data element path",
    )
    data_element_pattern: Optional[str] = Field(
        None,
        description="Pattern which matched this variable (if a pattern was used).",
        title="Data element pattern",
    )
    stable_identifier_type: Optional[str] = Field(
        None,
        description="Type of stable identifier the variable was mapped to prior to pseudonymization.",
        title="Stable identifier type",
    )
    stable_identifier_version: Optional[str] = Field(
        None,
        description="Version of stable identifier the variable was mapped to prior to pseudonymization.",
        title="Stable identifier version",
    )
    encryption_algorithm: Optional[str] = Field(
        None,
        description="The encryption algorithm used to pseudonymize the variable.",
        title="Encryption algorithm",
    )
    encryption_key_reference: Optional[str] = Field(
        None,
        description="Name of or reference to the encryption key used to pseudonymize the variable.",
        title="Encryption key reference",
    )
    encryption_algorithm_parameters: Optional[list[dict[str, Any]]] = Field(
        None,
        description="Parameters supplied to the encryption algorithm.",
        title="Encryption algorithm parameters",
    )
    source_variable: Optional[str] = Field(
        None, description="Short name of the source variable", title="Source variable"
    )
    source_variable_datatype: Optional[SourceVariableDataType] = Field(
        None,
        description="Data type of the variable prior to pseudonymization.",
        title="Source variable data type",
    )


class PseudonymizationMetadata(DatadocBaseModel):
    document_version: Literal["0.1.0"] = "0.1.0"
    pseudo_dataset: Optional[PseudoDataset] = None
    pseudo_variables: Optional[list[PseudoVariable]] = None


class Dataset(DatadocBaseModel):
    short_name: Optional[str] = Field(
        None,
        description="Name of (physical) data file, data table or dataset",
        title="Short name",
    )
    assessment: Optional[Assessment] = Field(
        None,
        description="Value assessment (sensitivity classification) for the data set",
        title="Assessment",
    )
    dataset_status: Optional[DataSetStatus] = Field(
        None, description="Life cycle for data set", title="Data set status"
    )
    dataset_state: Optional[DataSetState] = Field(
        None, description="Steady state of data", title="Data set state"
    )
    name: Optional[LanguageStringType] = Field(
        None, description="Name of data set", title="Name"
    )
    description: Optional[LanguageStringType] = Field(
        None, description="Free text description of the data set", title="Description"
    )
    data_source: Optional[str] = Field(
        None,
        description="Data source. Set either for the data set or instance variable.",
        title="Data source",
    )
    population_description: Optional[LanguageStringType] = Field(
        None,
        description="Description of the population covered in the data set. Includes unit type, spatial coverage and period of time.",
        title="Description of population",
    )
    version: Optional[str] = Field(
        None, description="Version of data set", title="Version"
    )
    version_description: Optional[LanguageStringType] = Field(
        None,
        description="Dataset version information in the form of descriptive text",
        title="Version description",
    )
    unit_type: Optional[str] = Field(
        None,
        description="Unit Type for data file, table or data set. See Definitions of Unit Types https://www.ssb.no/en/metadata/definisjoner-av-statistiske-enheter",
        title="Unit type",
    )
    temporality_type: Optional[TemporalityTypeType] = Field(
        None,
        description="Temporality type. Either for the instance variable or the data set",
        title="Temporality type",
    )
    subject_field: Optional[str] = Field(
        None,
        description="Primary area of statistics in which the data set is included",
        title="Subject field",
    )
    keyword: Optional[list[str]] = Field(
        None,
        description="A list of searchable keywords that can contribute to the development of effective filtering and search services.",
        title="Keyword(s)",
    )
    spatial_coverage_description: Optional[LanguageStringType] = Field(
        None,
        description="Description of the data set's spatial coverage",
        title="Spatial coverage description",
    )
    contains_personal_data: Optional[bool] = Field(
        None,
        description="Is there any personal data amongst this data (data set)?",
        title="Contains personal data",
    )
    use_restriction: Optional[UseRestriction] = Field(
        None, description="Data set use restriction", title="Use restriction"
    )
    use_restriction_date: Optional[AwareDatetime] = Field(
        None,
        description="Use restriction date, eg. the date (deadline) for when data must be deleted/anonymised.",
        title="Use restriction date",
    )
    custom_type: Optional[list[CustomTypeForDatasetMetadatum]] = Field(
        None,
        description="Extend the DataDoc model by adding custom metadata elements as key-value-pairs (string, array or objects).",
        title="Custom type for dataset metadata",
    )
    id: Optional[UUID] = Field(
        None, description="Unique identifier for the data set", title="Identifier"
    )
    owner: Optional[str] = Field(
        None,
        description="Owner of the data set (responsible division in Statistics Norway). Values defined by https://www.ssb.no/en/klass/klassifikasjoner/83",
        title="Owner",
    )
    file_path: Optional[str] = Field(
        None,
        description="The file path contains the data set's name and the path to where it is stored",
        title="File path",
    )
    metadata_created_date: Optional[AwareDatetime] = Field(
        None,
        description="Created date for metadata about the data set",
        title="Metadata created date",
    )
    metadata_created_by: Optional[str] = Field(
        None, description="Created by identifiable person.", title="Metadata created by"
    )
    metadata_last_updated_date: Optional[AwareDatetime] = Field(
        None,
        description="Last updated date for metadata about the dataset",
        title="Metadata last updated date",
    )
    metadata_last_updated_by: Optional[str] = Field(
        None,
        description="Last change made by identifiable person. ",
        title="Metadata last updated by",
    )
    contains_data_from: Optional[date] = Field(
        None,
        description="The data set contains data from date/time",
        title="Contains data from",
    )
    contains_data_until: Optional[date] = Field(
        None,
        description="The data set contains data up until date/time",
        title="Contains data up until",
    )


class OtherSpecialValue(DatadocBaseModel):
    code: Optional[str] = Field(None, description="Other value code", title="Code")
    name: Optional[LanguageStringType] = Field(
        None, description="Other value name (text)", title="Name"
    )
    valid_from: Optional[AwareDatetime] = Field(
        None, description="Other value valid from date", title="Valid from"
    )
    valid_until: Optional[AwareDatetime] = Field(
        None, description="Other value until date", title="Valid until"
    )


class SpecialValues(DatadocBaseModel):
    sentinel: Optional[SentinelValues] = Field(None, title="Sentinel values")
    other_value: Optional[list[OtherSpecialValue]] = Field(
        None,
        description="Other special values not represented as 'sentinel_value' in a standardized code list.",
        title="Other special values",
    )


class Variable(DatadocBaseModel):
    short_name: Optional[str] = Field(
        None,
        description="Physical name of the variable (data element) in the dataset. Should match the recommended short name.",
        title="Short name",
    )
    data_element_path: Optional[str] = Field(
        None,
        description="The path (dot notation) to the data element in a hierarchical data structure, eg. 'person.adress'. Must be given in addition to the short_name.",
        title="Data element path",
    )
    name: Optional[LanguageStringType] = Field(
        None,
        description="Variable names can be inherited from VarDef, but can also be documented/changed here",
        title="Name",
    )
    data_type: Optional[DataType] = Field(
        None, description="Data type", title="Data type"
    )
    variable_role: Optional[VariableRole] = Field(
        None,
        description="Role of the instance variable in the data set",
        title="Variable role",
    )
    definition_uri: Optional[AnyUrl] = Field(
        None,
        description="A link (URI) to the variable's definition in Vardok/VarDef",
        title="Definition URI",
    )
    is_personal_data: Optional[IsPersonalData] = Field(None, description="", title="")
    data_source: Optional[str] = Field(
        None,
        description="Data source. Set at data set level, but can be overwritten at variable instance level.",
        title="Data source",
    )
    population_description: Optional[LanguageStringType] = Field(
        None,
        description="The population the variable describes can be specified in more detail here. Set at dataset level, but can be overwritten at instance variable level.",
        title="Population description",
    )
    comment: Optional[LanguageStringType] = Field(
        None,
        description="Further clarification of the variables definition",
        title="Comment",
    )
    temporality_type: Optional[TemporalityTypeType] = Field(
        None,
        description="Temporality type. Set either for variable instance or dataset.",
        title="Temporality type",
    )
    measurement_unit: Optional[str] = Field(
        None, description="Measurement unit", title="Measurement unit"
    )
    multiplication_factor: Optional[int] = Field(
        None,
        description="A multiplication factor for a value/result is a number that multiplies that value/result.",
        title="Multiplication factor",
    )
    format: Optional[str] = Field(
        None,
        description="The format of the values \u200b\u200b(physical format or regular expression) in machine-readable form for validation. This can be used as a further specification of the data type (dataType) in those cases where this is relevant.",
        title="Format",
    )
    classification_uri: Optional[AnyUrl] = Field(
        None,
        description="Link (URI) to valid classification or code list",
        title="Classification or codelist URI",
    )
    special_value: Optional[SpecialValues] = Field(None, title="Special values")
    invalid_value_description: Optional[LanguageStringType] = Field(
        None,
        description="Invalid value(s) description used in addition (or as an alternative) to standard sentinel values.",
        title="Invalid value(s) description",
    )
    custom_type: Optional[list[CustomTypeForVariableMetadatum]] = Field(
        None,
        description="Extend the DataDoc model by adding custom metadata elements as key-value-pairs (string, array or objects).",
        title="Custom type for variable metadata",
    )
    id: Optional[UUID] = Field(
        None,
        description="Unique SSB identifier for the instance variable in the data set",
        title="Identifier",
    )
    contains_data_from: Optional[date] = Field(
        None,
        description="The instance variable in the data set contains data from and including this date. This can be useful information for data sets that contain many instance variables in addition to data for many periods/years. In many cases, it will then be the case that some variables only contain data for the most recent periods/years, e.g. if the entire data set contains data from 1970 to 2020, while some instance variables only contain data from 1998 onwards.",
        title="Contains data from",
    )
    contains_data_until: Optional[date] = Field(
        None,
        description="The instance variable in the data set contains data up to and including this date. This can be useful information for data sets that contain many instance variables in addition to data for many periods/years. In many cases, it will then be the case that some of the instance variables in the data set are terminated (no longer updated) after a given point in time.",
        title="Contains data up until",
    )


class DatadocMetadata(DatadocBaseModel):
    percentage_complete: Optional[int] = Field(
        None, description="Percentage of obligatory metadata fields populated."
    )
    document_version: Literal["3.3.0"] = Field(
        "3.3.0", description="Version of this model"
    )
    dataset: Optional[Dataset] = None
    variables: Optional[list[Variable]] = None


class MetadataContainer(DatadocBaseModel):
    document_version: Literal["0.0.1"] = "0.0.1"
    datadoc: Optional[DatadocMetadata] = None
    pseudonymization: Optional[PseudonymizationMetadata] = None
