package ADT.adt.model;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

import java.util.Date;

@Entity
@Table(name="ManagementUnit")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class ManagementUnit {
    private int id;
    private String name;
    private String address;
    private String phoneNumber;
    private String email;
    private Date establishmentDate;
    private String director;
    private String specializations;

}
