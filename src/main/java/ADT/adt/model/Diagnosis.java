package ADT.adt.model;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="Diagnosis")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Diagnosis {
    private int id;
    private int patientId;
    private int doctorId;
    private Date admissionDate;
    private String reasonForAdmission;
    private String diagnosticTests;
    private String diagnosis;
    private String treatmentPlan;


}
