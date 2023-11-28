package ADT.adt;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FrontPageController {
    @GetMapping("/")
    public String index(){
        return "gfdg";
    }
}
