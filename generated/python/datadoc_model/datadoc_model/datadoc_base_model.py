from pydantic import ConfigDict, BaseModel


class DatadocBaseModel(BaseModel):
    """Defines configuration which applies to all Models in this package."""

    model_config = ConfigDict(validate_assignment=True, use_enum_values=True)