package ADT.adt.model;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="Patient")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Patient {
    private int id;
    private String firstName;
    private String lastName;
    private String pesel;
    private Date dateOfBirth;
    private boolean sex;
    private String telephone;
    private String bloodGroup;
    private String chronicDiseases;
    private String medicalAllergy;
    private String addressCity;
    private String addressNumber;
}
