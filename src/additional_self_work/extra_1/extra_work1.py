"""
Многочлен P(x)=a_nx^n+a_(n−1)x^n−1+...+a_1x+a_0 с целыми коэффициентами можно представить в виде списка. 
При этом, если ai=0, то соответствующий элемент не включается в список. 
На рисунке показано общее представление многочлена и пример для S(x)=−5x_6+3x_2−x+7:

Необходимо описать тип данных, соответствующий предложенному представлению многочленов, а также разработать процедуру Add(P,Q,R) 
вычисления суммы многочленов Q и R, результат – многочлен P.
"""


class PolyNode:
    def __init__(self, coefficient=0, power=0):
        self.coefficient = coefficient
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, power):
        new_node = PolyNode(coefficient, power)
        if not self.head or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.power >= power:
                current = current.next
            if current.power == power:
                current.coefficient += coefficient
            else:
                new_node.next = current.next
                current.next = new_node

    def print_polynomial(self):
        current = self.head
        if not current:
            print("0")
            return
        terms = []
        first_term = True

        while current:
            if current.power == 0:
                term = f"{current.coefficient}"
            elif current.coefficient == 1:
                term = f"x^{current.power}" if current.power > 1 else "x"
            elif current.coefficient == -1:
                term = f"-x^{current.power}" if current.power > 1 else "-x"
            else:
                term = (
                    f"{current.coefficient}x^{current.power}"
                    if current.power > 1
                    else f"{current.coefficient}x"
                )

            if first_term:
                terms.append(term)
                first_term = False
            else:
                if current.coefficient < 0:
                    terms.append(
                        f"- {term[1:]}" if term.startswith("-") else f"- {term}"
                    )
                else:
                    terms.append(f"+ {term}")

            current = current.next

        print(" ".join(terms))

    def add(self, R):
        P = Polynomial()
        q_node = self.head
        r_node = R.head

        while q_node or r_node:
            if q_node and (not r_node or q_node.power > r_node.power):
                P.add_term(q_node.coefficient, q_node.power)
                q_node = q_node.next
            elif r_node and (not q_node or r_node.power > q_node.power):
                P.add_term(r_node.coefficient, r_node.power)
                r_node = r_node.next
            else:
                new_coeff = q_node.coefficient + r_node.coefficient
                if new_coeff != 0:
                    P.add_term(new_coeff, q_node.power)
                q_node = q_node.next
                r_node = r_node.next

        return P


# def input_polynomial():
#     poly = Polynomial()
#     print(
#         "Введите члены многочлена (коэффициент и степень). Для завершения введите 'stop'."
#     )
#     while True:
#         coeff_input = input("Введите коэффициент: ")
#         if coeff_input.lower() == "stop":
#             break
#         power_input = input("Введите степень: ")
#         if power_input.lower() == "stop":
#             break
#         try:
#             coefficient = int(coeff_input)
#             power = int(power_input)
#             poly.add_term(coefficient, power)
#         except ValueError:
#             print("Неправильный ввод. Попробуйте снова.")
#     return poly


def main():
    Q = Polynomial()
    Q.add_term(-5, 3)
    Q.add_term(3, 2)
    Q.add_term(-1, 1)
    Q.add_term(7, 0)

    R = Polynomial()
    R.add_term(6, 3)
    R.add_term(2, 2)
    R.add_term(1, 1)

    P = Q.add(R)

    print("Q(x) = ", end="")
    Q.print_polynomial()
    print("R(x) = ", end="")
    R.print_polynomial()
    print("P(x) = Q(x) + R(x) = ", end="")
    P.print_polynomial()


if __name__ == "__main__":
    main()
