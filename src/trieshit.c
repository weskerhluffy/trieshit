/*
 * 
 *
 *  Created on: 27/10/2017
 *      Author: 
 */

// XXX: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

typedef struct nt {
	char c;
	struct nt *v['z' - 'a' + 1];
	int cont;
} nt;

nt *nds = NULL;
int ndsc = 0;

#define max(a,b) (a>b?a:b)

void ac(nt *r, char *n, int nc, int v) {
	nt *na = r;
//    printf("mierda %s tam %d\n",n,nc);
	for (int i = 0; i < nc; i++) {
		char ca = n[i] - 'a';
		if (na->v[ca]) {
			na = na->v[ca];
		} else {
			nt *nn = nds + ndsc++;
			na->v[ca] = nn;
//            printf("anadiendo nodo %c a %c\n",ca,na->c);
			na = nn;
		}
		na->c = ca;
		na->cont = max(na->cont, v);
	}
}

int ec(nt *r, char *n, int nc) {
	nt *na = r;
	int i;
	for (i = 0; i < nc; i++) {
		char ca = n[i] - 'a';
//        printf("letra act %c en %c\n",ca,na->c);
		if (na->v[ca]) {
			na = na->v[ca];
		} else {
			break;
		}
	}
//    printf("el ult nodo '%c' u %u nc %u\n",na->c,i,nc);
	return i == nc ? na->cont : 0;
}

int main() {

	int caca = 0;
	int ass = 0;
	int valor = 0;
//    nds=calloc((((int)1E5)+1)*22,sizeof(nt));
	nds = calloc(100000 * 10, sizeof(nt));
	assert(nds);
	char *palo = NULL;

	palo = calloc(((int) 1E6 + 1), sizeof(char));
	assert(palo);

	scanf("%d %d", &caca, &ass);
	nt *raiz = nds + ndsc++;

	while (caca--) {
		scanf("%s %d", palo, &valor);
//        printf("la op %s\n",op);
		ac(raiz, palo, strlen(palo), valor);
	}

	while (ass--) {
		scanf("%s", palo);
		int mierda = ec(raiz, palo, strlen(palo));
		printf("%u\n", mierda);
	}

	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	return 0;
}

