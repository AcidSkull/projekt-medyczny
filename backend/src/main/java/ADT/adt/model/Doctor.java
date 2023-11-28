package ADT.adt.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

@Entity
@Table(name="Doctor")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Doctor {
    private int id;
    private String firstName;
    private String lastName;
    private String specialization;

}
