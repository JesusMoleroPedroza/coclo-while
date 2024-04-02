package vectores;

import java.util.ArrayList;
import java.util.Collections;

public class Vectores {

    public static void main(String[] args) {
        
        /*JESUS MOLERO*/
        
        /*1*/
        ArrayList<String> lista = new ArrayList();
        System.out.println(lista);
        
        /*2*/
        ArrayList<Integer> lista2 = new ArrayList();
        lista2.add(0,12);
        lista2.add(1,38);
        lista2.add(2,11);
        lista2.add(3,20);
        lista2.add(4,77);
        lista2.add(5,50);
        lista2.add(6,32);
        System.out.println(lista2);
        
        /*3*/
        System.out.println(lista2.size());
        
        /*4*/
        System.out.println(lista2.get(0)+" "+lista2.get(3)+" "+lista2.get(6));
        
        /*5*/
        ArrayList<Object> listaMezclada = new ArrayList();
        listaMezclada.add(0,"jesus molero");
        listaMezclada.add(1,20);
        listaMezclada.add(2, 1.80);
        listaMezclada.add(3,"soltero");
        listaMezclada.add(4,"Bayunca");
        System.out.println(listaMezclada);
        
        /*6*/
        ArrayList<String> it_company = new ArrayList();
        it_company.add("Facebook");
        it_company.add("Google");
        it_company.add("Microsoft");
        it_company.add("Apple");
        it_company.add("IBM");
        it_company.add("oracle");
        it_company.add("Amazon");
        System.out.println(it_company);
        
        /*7*/
        it_company.add("Instagram");
        System.out.println(it_company);
        
        /*8*/
        System.out.println("la lista contiene Google: "+it_company.contains("Google"));
        
        /*9*/
        Collections.sort(it_company);
        System.out.println(it_company);
        
        /*10*/
        Collections.reverse(it_company);
        System.out.println("invercion de lista: "+it_company);
        
        /*11*/
        it_company.remove(0);
        System.out.println(it_company);
        
        /*12*/
        it_company.clear();
        System.out.println(it_company);
    }
    
}
