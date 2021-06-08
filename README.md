# projeto_aa2
Identificação de documentos similares/relevantes para cancro do estômago

Projeto C.3 - Aprendizagem Automática 2
Orientadores : Rúben Rodrigues e Nuno Alves

* Pequena anotação

A execução deste notebook não é rápida por isso caso pretendam aceder aos ficheiros resultantes da mesma podem encontrá-los neste link.
https://we.tl/t-zOAS5eXoiN

* Contextualização

Repositórios como o PUBMED contêm mais de 30 milhões de documentos que estão indexados a termos chave. Estes repositórios possibilitam a identificação de documentos relevantes sobre um determinado termo.


* Problema

Existem documentos que são relevantes a um determinado tópico, mas que não estão devidamente identificados.

* Solução

Existem abordagens baseadas em aprendizagem máquina não supervisionadas como a Latent Dirichlet Allocation (LDA) em que é possível aplicar o cálculo da distância Jensen-Shannon para identificar documentos similares a um determinado tópico. Exemplos de pesquisas que podem beneficiar de um sistema orientado a similaridade de documentos incluem a pesquisa sobre uma determinada doença como o cancro do estômago e um tratamento que não foi indexado pelo repositório.

* Objetivo

Implementar uma pipeline em python que calcule a similaridade de documentos recorrendo ao LDA e à fórmula de Jensen-Shannon e integrem a pipeline desenvolvida na framework do grupo BioSystems (BioTMpy).


* Execução:

Todos o nosso trabalho realizado encontra-se no ficheiro notebook.ipynb e deve ser executado sequencialmente
