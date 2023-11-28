package ADT.adt.model;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="HospitalStay")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class HospitalStay {
    private Date admissionDate;
    private Date dischargeDate;
    private String medicalProcedures;
    private int doctorId;
    private int nurseId;
    private String additionalInfo;
    private int diagnosisId;
    private int id;
    private int unitId;
    private int roomId;
    private int patientId;
    private int wardId;

}
