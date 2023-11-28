package ADT.adt.model;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="Appointment")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Appointment {
    private int id;
    private int doctorId;
    private int patientId;
    private Date date;
    private String goalOfAppointment;

}

