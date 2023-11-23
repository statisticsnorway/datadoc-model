
package no.ssb.dapla.metadata;

import java.io.Serializable;
import java.util.LinkedHashMap;
import java.util.Map;
import javax.annotation.processing.Generated;
import javax.validation.Valid;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import no.ssb.dapla.metadata.datadoc.DatadocJsonSchema;


/**
 * Metadata container
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "document_version",
    "datadoc",
    "pseudonymization"
})
@Generated("jsonschema2pojo")
public class MetadataContainerJsonSchema implements Serializable
{

    /**
     * Version of this model
     * 
     */
    @JsonProperty("document_version")
    private Object documentVersion;
    /**
     * Datadoc metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("datadoc")
    @Valid
    private DatadocJsonSchema datadoc;
    /**
     * Pseudonymization metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("pseudonymization")
    @Valid
    private PseudonymizationJsonSchema pseudonymization;
    @JsonIgnore
    @Valid
    private Map<String, Object> additionalProperties = new LinkedHashMap<String, Object>();
    private final static long serialVersionUID = -7643741090930903820L;

    /**
     * No args constructor for use in serialization
     * 
     */
    public MetadataContainerJsonSchema() {
    }

    public MetadataContainerJsonSchema(Object documentVersion, DatadocJsonSchema datadoc, PseudonymizationJsonSchema pseudonymization) {
        super();
        this.documentVersion = documentVersion;
        this.datadoc = datadoc;
        this.pseudonymization = pseudonymization;
    }

    /**
     * Version of this model
     * 
     */
    @JsonProperty("document_version")
    public Object getDocumentVersion() {
        return documentVersion;
    }

    /**
     * Version of this model
     * 
     */
    @JsonProperty("document_version")
    public void setDocumentVersion(Object documentVersion) {
        this.documentVersion = documentVersion;
    }

    /**
     * Datadoc metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("datadoc")
    public DatadocJsonSchema getDatadoc() {
        return datadoc;
    }

    /**
     * Datadoc metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("datadoc")
    public void setDatadoc(DatadocJsonSchema datadoc) {
        this.datadoc = datadoc;
    }

    /**
     * Pseudonymization metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("pseudonymization")
    public PseudonymizationJsonSchema getPseudonymization() {
        return pseudonymization;
    }

    /**
     * Pseudonymization metadata
     * <p>
     * 
     * 
     */
    @JsonProperty("pseudonymization")
    public void setPseudonymization(PseudonymizationJsonSchema pseudonymization) {
        this.pseudonymization = pseudonymization;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(MetadataContainerJsonSchema.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("documentVersion");
        sb.append('=');
        sb.append(((this.documentVersion == null)?"<null>":this.documentVersion));
        sb.append(',');
        sb.append("datadoc");
        sb.append('=');
        sb.append(((this.datadoc == null)?"<null>":this.datadoc));
        sb.append(',');
        sb.append("pseudonymization");
        sb.append('=');
        sb.append(((this.pseudonymization == null)?"<null>":this.pseudonymization));
        sb.append(',');
        sb.append("additionalProperties");
        sb.append('=');
        sb.append(((this.additionalProperties == null)?"<null>":this.additionalProperties));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.datadoc == null)? 0 :this.datadoc.hashCode()));
        result = ((result* 31)+((this.additionalProperties == null)? 0 :this.additionalProperties.hashCode()));
        result = ((result* 31)+((this.pseudonymization == null)? 0 :this.pseudonymization.hashCode()));
        result = ((result* 31)+((this.documentVersion == null)? 0 :this.documentVersion.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MetadataContainerJsonSchema) == false) {
            return false;
        }
        MetadataContainerJsonSchema rhs = ((MetadataContainerJsonSchema) other);
        return (((((this.datadoc == rhs.datadoc)||((this.datadoc!= null)&&this.datadoc.equals(rhs.datadoc)))&&((this.additionalProperties == rhs.additionalProperties)||((this.additionalProperties!= null)&&this.additionalProperties.equals(rhs.additionalProperties))))&&((this.pseudonymization == rhs.pseudonymization)||((this.pseudonymization!= null)&&this.pseudonymization.equals(rhs.pseudonymization))))&&((this.documentVersion == rhs.documentVersion)||((this.documentVersion!= null)&&this.documentVersion.equals(rhs.documentVersion))));
    }

}
