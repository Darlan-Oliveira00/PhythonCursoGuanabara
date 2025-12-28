import java.util.Scanner;

public class SomaDoisNumeros {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int num1 = entrada.nextInt();

        System.out.print("Digite o segundo número: ");
        int num2 = entrada.nextInt();

        int soma = num1 + num2;

        System.out.println("A soma dos dois números é: " + soma);

        entrada.close();
    }
}