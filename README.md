# BST

📄 [View Full Report (PDF)](AllSkeleton_BTS.pdf)

<img align= "center" str= "https://github.com/chevil-dev/AllSkeleton_BST/images/00.png" width= "300">

# Analysis et Algorithmus Generandi Arbores Quaestorias Binarias (BST)

Hoc opus analysis et implementationem algorithmorum continet ad omnes arbores quaesitorias binarias (BST) possibiles ex dato numerorum ordine construendas. Praeterea, hic est expositio mathematica, quae demonstrat veritatem formulae ad numerum harum arborum computandum, quae sunt numeri Catalani.

Hoc relatum, ex articulo a **Arman Riazi** scripto, paratum est et includit algorithmos, codicem in Python, et explicationes mathematicas.

## 📝 Summa Contenti Imaginum

Imagines partes articuli technici vel relationis sunt, quae in tres sectiones principales dividuntur:

1.  **Prima Imago:** Introductio auctoris (Arman Riazi) et tituli articuli. Etiam, primus algorithmus, `AllSkeleton(start, end)`, ad omnes sceleta arborum BST ex numeris sequentibus construenda, cum sua implementatione in Python, praebetur.

2.  **Secunda Imago:** Continuatio explicationis algorithmorum et praebitio formulae recurrentis ad numerum arborum computandum. Haec formula est clarissima relatio numerorum Catalanorum: $T(n) = \sum_{i=1}^{n} T(i-1) T(n-i)$ . Deinde, functio generans pro hac relatione definitur et solvitur.

3.  **Tertia Imago:** Ultima pars demonstrationis mathematicae. Hac in sectione, usus fit theorematis binomialis generalizati ad extrahendum formulam clausam numerorum Catalanorum ex functione generante. Resultatum finale est formula nota: $C_n = \frac{1}{n+1} \binom{2n}{n}$.

## 💻 Algorithmus et Implementatio

Principalis algorithmus ad omnes arbores generandas recursive operatur.

### Algorithmus `AllSkeleton(start, end)`

Haec functio omnes BST possibiles pro numeris sequentibus ab `start` ad `end` generat.

* **Modus Operandi:** Pro omni numero `i` in ambitu `[start, end]`, `i` ut radix consideratur. Deinde, recursive omnes subarbores sinistras (pro numeris `[start, i-1]`) et subarbores dextras (pro numeris `[i+1, end]`) generat. Denique, combinando omnes subarbores sinistras et dextras, omnes arbores possibiles construuntur.

### Codex in Python

Infra est codex plenus algorithmorum cum simplici classe ad nodum (Node) definiendum:

```python
class Node:
    """Classis ad nodum in arbore repraesentandum."""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def allSkeleton(start: int, end: int) -> list[Node]:
    """
    Functio recursiva ad omnes sceleta arborum BST generanda.

    Args:
        start: Numerus initii ambitus (inclusivus).
        end: Numerus finis ambitus (inclusivus).

    Returns:
        Index nodorum radicum, ubi unusquisque nodus unam BST unicam repraesentat.
    """
    if start > end:
        return [None]
    
    allTrees = []
    for i in range(start, end + 1):
        leftTrees = allSkeleton(start, i - 1)
        rightTrees = allSkeleton(i + 1, end)
        
        for left in leftTrees:
            for right in rightTrees:
                currentNode = Node(i)
                currentNode.left = left
                currentNode.right = right
                allTrees.append(currentNode)
                
    return allTrees

```

## 📐 Demonstratio Mathematica: Numeri Catalani

<img align= "center" str= "https://github.com/chevil-dev/AllSkeleton_BST/images/01.png" width= "300">

Numerus totalis BST, qui cum `n` nodis construi potest, per numeros Catalanos computatur. Infra, demonstratio in imaginibus praebita summatim exponitur.

### Relatio Recurrens

Numerus arborum $T(n)$ per hanc relationem recurrentem ostendi potest, quae directe ex algorithmus construendi arbores derivatur:

$$T(n) = \sum_{i=1}^{n} T(i-1) T(n-i) \quad \text{pro } n \geq 1$$
$$T(0) = 1$$

### Functio Generans

Utendo functione generante $B(x) = \sum_{n=0}^{\infty} T(n) x^n$ et solvendo relationem recurrentem, ad hanc formulam clausam pervenimus:

$$B(x) = \frac{1 - \sqrt{1-4x}}{2x}$$

### Formula Finalis

Utendo expansionem serierum Taylor pro functione supra, coefficientes $x^n$, qui sunt $T(n)$, obtinentur, quod est formula finalis numerorum Catalanorum:

$$T(n) = \frac{1}{n+1} \binom{2n}{n}$$
