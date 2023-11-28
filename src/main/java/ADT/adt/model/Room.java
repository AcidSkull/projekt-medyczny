package ADT.adt.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.*;

@Entity
@Table(name="Room")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@ToString
public class Room {
    private int id;
    private int wardId;
}
