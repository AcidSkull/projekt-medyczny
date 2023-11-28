package ADT.adt.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

@Entity
@Table(name="Ward")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Ward {
    private int id;
    private String name;
    private int number;
}
