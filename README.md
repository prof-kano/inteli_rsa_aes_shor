# MINI CTF - RSA, Quebra e Algoritmo de Shor

## Introdução
Este repositório contém os materiais necessários para a execução da atividade prática do dia 11/12/2024 da disciplina optativa de Quantum Safe do Instituto de Tecnologia e Liderança (Inteli).

## Ideia Principal do Ataque 

O módulo público _n_ é igual a um número primo _p_ vezes um número primo _q_. Se você conhece _p_ e _q_ (e _e_ da chave pública), poderá determinar a chave privada, quebrando assim a criptografia. No entanto, fatorar um _n_ grande para achar _p_ e _q_ é muito difícil sem o uso de um computador quântico eficiente. Um _n_ pequeno, talvez, possa ser fatorado através do Algoritmo de Shor em um computador quântico disponível agora. Vamos descobrir! 

A ideia básica do ataque consiste em fatorizar _n_ (que é público), dessa forma, o atacante pode derivar a chave privada (_d_) com _p_, _q_, e _e_ através da seguinte relação _d ≡ e^-1 mod Φ(n)_. Lembrando que _Φ(n)=(p-1)×(q-1)_. 

## Cenário Reduzido para Quebra

Para fins didáticos, cada primo _p_ e _q_ é gerado com 8 bits, conforme a chamada padrão da função generate_prime(bits=8).

O tamanho de _n_ será aproximadamente a soma dos tamanhos de _p_ e _q_.

A chave privada é composta por _n_ e _d_. O tamanho de _n_ determina o tamanho da chave RSA, que é de aproximadamente 16 bits nesse caso.
O valor de _d_ (o expoente da chave privada) é menos previsível em tamanho exato, mas geralmente será de um tamanho comparável ao de 
_𝜙(n)_ que é um pouco menos de 16 bits neste exemplo.

• Uma visão geral dos tamanhos de chaves RSA comumente usados:

1024 bits

2048 bits

3072 bits

4096 bits

## Fluxo da Dinâmica
![alice bob carlos drawio](https://github.com/user-attachments/assets/b656db96-39d7-4428-859f-ce014e5995da)

## Atividade

### • Mensagem Secreta

Junto com seu grupo, combinem uma frase secreta (sem caracteres especiais) que não deve ser compartilhada com nenhum outro grupo. 

![image](https://github.com/user-attachments/assets/950254f6-fac5-47fa-adc5-202e978a3cb4)

Substitua a frase padrão do trecho do código do programa Alice_Bob.py pela frase escolhida pelo grupo. 

### • Canal de Comunicação Simulado
Iremos utilizar um drive aberto para que cada grupo disponibilize os dados considerados públicos em uma comunicação:
#### https://drive.google.com/drive/folders/15dsGyEeDWbrR268lTc6S-Et531BGVeLy?usp=sharing
Crie uma pasta com o nome do seu grupo e dentro dela faça o upload da pasta "public" resultante da execução do programa "Alice_Bob". 
Acesse e copie a pasta "public" disponibilizada por cada grupo. 

### • CTF

O programa Carlos.py apresenta uma versão incompleta do ataque descrito na imagem do fluxo. Tente usar ou implementar função de fatoração usando o algoritmo de Shor da biblioteca do Qiskit ou similar. 
Com isso, você conseguirá recuperar a chave privada do RSA e, consequentemente, a chave do AES. Tendo acesso a mensagem secreta dos outros grupos. 

https://www.youtube.com/watch?v=mAHC1dWKNYE&list=PLkzEMll7nz0WNdePloNqT0YkGIO7iQrig

### • DICA DO CTF
 
Não será tão fácil como importar uma simples função. Você verá a dificuldade de lidar com assuntos do estado da arte. 

### • INTERVALO DISCUSSÃO DE DIFICULDADES ENCONTRADAS

Spoiler - Discutir em Aula

https://docs.quantum.ibm.com/api/qiskit/0.25/qiskit.algorithms.Shor

https://github.com/qiskit-community/qiskit-algorithms

### • OPORTUNIDADE DE FAZER A DIFERENÇA

### • QUEBRA PADRÃO e CONCLUSÃO

