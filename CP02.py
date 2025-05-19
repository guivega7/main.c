/*
Guilherme Vega RM:562655
Gabriel Pereira RM:563571
Luiz Henrique Araujo RM:563795
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Protótipos das funções
void fibonacci();
void fatoriais();
void verificaPalindromo();
void verificaSubstring();

int main() {
    int opcao;

    printf("===== MENU DE EXERCÍCIOS =====\n");
    printf("1 - Sequência de Fibonacci\n");
    printf("2 - Fatoriais\n");
    printf("3 - Verificar Palíndromo\n");
    printf("4 - Verificar Substring\n");
    printf("Escolha uma opção: ");
    scanf("%d", &opcao);

    // Limpar buffer do teclado para evitar problemas com fgets depois de scanf
    while(getchar() != '\n');

    switch (opcao) {
        case 1:
            fibonacci();
            break;
        case 2:
            fatoriais();
            break;
        case 3:
            verificaPalindromo();
            break;
        case 4:
            verificaSubstring();
            break;
        default:
            printf("Opção inválida.\n");
    }

    return 0;
}

void fibonacci() {
    int N;

    do {
        printf("Digite a quantidade de termos da sequência de Fibonacci (1 a 50): ");
        scanf("%d", &N);
    } while (N < 1 || N > 50);

    int fib[N];

    // Preencher a sequência
    fib[0] = 0;
    if (N > 1) fib[1] = 1;
    for (int i = 2; i < N; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    printf("Sequência de Fibonacci: ");
    for (int i = 0; i < N; i++) {
        printf("%d ", fib[i]);
    }
    printf("\n");
}

void fatoriais() {
    int N;

    do {
        printf("Digite um número inteiro (1 a 20): ");
        scanf("%d", &N);
    } while (N < 1 || N > 20);

    unsigned long long fat[N];  // Usar unsigned long long para suportar até 20!

    fat[0] = 1; // 1! = 1
    for (int i = 1; i < N; i++) {
        fat[i] = fat[i-1] * (i+1);
    }

    printf("Fatoriais:\n");
    for (int i = 0; i < N; i++) {
        printf("%d! = %llu\n", i+1, fat[i]);
    }
}

void verificaPalindromo() {
    char palavra[101];

    printf("Digite uma palavra: ");
    scanf("%100s", palavra);

    int tamanho = strlen(palavra);
    int ehPalindromo = 1;

    for (int i = 0; i < tamanho / 2; i++) {
        // Considerar case insensitive
        if (tolower(palavra[i]) != tolower(palavra[tamanho - 1 - i])) {
            ehPalindromo = 0;
            break;
        }
    }

    if (ehPalindromo)
        printf("A palavra é um palíndromo.\n");
    else
        printf("A palavra NÃO é um palíndromo.\n");
}

void verificaSubstring() {
    char str1[201];
    char str2[201];

    printf("Digite a primeira string: ");
    fgets(str1, sizeof(str1), stdin);
    // Remove '\n' do final se existir
    str1[strcspn(str1, "\n")] = 0;

    printf("Digite a segunda string: ");
    fgets(str2, sizeof(str2), stdin);
    str2[strcspn(str2, "\n")] = 0;

    // Usar strstr para verificar substring
    if (strstr(str1, str2) != NULL)
        printf("A segunda string está contida na primeira.\n");
    else
        printf("A segunda string NÃO está contida na primeira.\n");
}
