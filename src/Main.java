import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Copie Ou Digite o Caminho do Seu Arquivo : "); //testar com o arquivo na msm pasta
        try {
            String path = sc.nextLine();
            System.out.print("Qual o Formato do Seu Arquivo Atualmente(Formatos Compativeis = PDF,TXT,DOCX): ");
            String origin = sc.nextLine().trim().toLowerCase();
            System.out.print("Para Qual Formato Deseja Converter (1 = pdf | 2 = txt | 3 = docx | 4 = pptx ): ");
            String finale = sc.nextLine();

            ProcessBuilder ps = new ProcessBuilder(".\\src\\dist_python\\main.exe", finale,origin,path);
            ps.redirectErrorStream(true);
            Process process = ps.start();
            try (BufferedReader ln = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line = ln.readLine();
                System.out.println(line);
            }

        }catch (RuntimeException e ){
            System.out.print("Erro Na URL:");
            e.printStackTrace();
        }





        sc.close();


    }
}