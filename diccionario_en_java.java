package diccionario_en_java;

import java.util.*;

public class diccionario_en_java{
    
    public static void main(String[] args) {
        // #1
        HashMap<String, String> perro = new HashMap<>();
        System.out.println(perro);
        System.out.println();

        // #2
        perro.put("nombre", "luna");
        perro.put("color", "Marrón");
        perro.put("raza", "pitbull");
        perro.put("patas", "4");
        perro.put("edad", "1 año");
        System.out.println(perro);
        System.out.println();

        // #3
        HashMap<String, Object> estudiante = new HashMap<>();
        estudiante.put("nombre", "jesus");
        estudiante.put("apellido", "molero");
        estudiante.put("sexo", "Masculino");
        estudiante.put("edad", "20");
        estudiante.put("estado civil", "Soltero");
        List<String> habilidades = new ArrayList<>();
        habilidades.add("Programar php");
        habilidades.add("Programar c++");
        estudiante.put("habilidades", habilidades);
        estudiante.put("pais", "Colombia");
        estudiante.put("ciudad", "Cartagena");
        estudiante.put("direccion", "bayunca");
        System.out.println(estudiante);
        System.out.println();

        // #4
        System.out.println(estudiante.size());
        System.out.println();

        // #5
        System.out.println(estudiante.get("habilidades"));
        System.out.println(estudiante.get("habilidades").getClass());
        System.out.println();

        // #6
        List<String> habilidadesEstudiante = (List<String>) estudiante.get("habilidades");
        habilidadesEstudiante.add("programar python");
        System.out.println(estudiante);
        System.out.println();

        // #7
        Set<String> keys = estudiante.keySet();
        System.out.println(keys);
        System.out.println();

        // #8
        Collection<Object> values = estudiante.values();
        System.out.println(values);
        System.out.println();

        // #9
        Set<Map.Entry<String, Object>> entries = estudiante.entrySet();
        System.out.println(entries);
        System.out.println();

        // #10
        estudiante.remove("pais");
        System.out.println(estudiante);
        System.out.println();

        // #11;
        estudiante = null;
        System.out.println();
    }
}
