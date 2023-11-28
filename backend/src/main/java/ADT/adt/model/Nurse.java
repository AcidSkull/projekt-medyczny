package ADT.adt.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

@Entity
@Table(name="Nurse")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Nurse {
    private int id;
    private String firstName;
    private String lastName;

}
