from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt


class washing_machine:
    # Inputs and Outputs
    degree_of_dirt = ctrl.Antecedent(np.arange(0, 101, 1), "degree_of_dirt")
    type_of_dirt = ctrl.Antecedent(np.arange(0, 101, 1), "type_of_dirt")
    wash_time = ctrl.Consequent(np.arange(0, 61, 1), "wash_time")

    # keys for plot
    degree_names = ["Low", "Medium", "High"]
    type_names = ["NonFat", "Medium", "Fat"]

    # Outputing them into auto-membership functions
    degree_of_dirt.automf(names=degree_names)
    type_of_dirt.automf(names=type_names)

    # Washing Time Universe
    wash_time["very_short"] = fuzz.trimf(wash_time.universe, [0, 8, 12])
    wash_time["short"] = fuzz.trimf(wash_time.universe, [8, 12, 20])
    wash_time["medium"] = fuzz.trimf(wash_time.universe, [12, 20, 40])
    wash_time["long"] = fuzz.trimf(wash_time.universe, [20, 40, 60])
    wash_time["very_long"] = fuzz.trimf(wash_time.universe, [40, 60, 60])

    # Rules Applied
    rule1 = ctrl.Rule(
        degree_of_dirt["High"] | type_of_dirt["Fat"], wash_time["very_long"]
    )
    rule2 = ctrl.Rule(degree_of_dirt["Medium"] | type_of_dirt["Fat"], wash_time["long"])
    rule3 = ctrl.Rule(degree_of_dirt["Low"] | type_of_dirt["Fat"], wash_time["long"])
    rule4 = ctrl.Rule(
        degree_of_dirt["High"] | type_of_dirt["Medium"], wash_time["long"]
    )
    rule5 = ctrl.Rule(
        degree_of_dirt["Medium"] | type_of_dirt["Medium"], wash_time["medium"]
    )
    rule6 = ctrl.Rule(
        degree_of_dirt["Low"] | type_of_dirt["Medium"], wash_time["medium"]
    )
    rule7 = ctrl.Rule(
        degree_of_dirt["High"] | type_of_dirt["NonFat"], wash_time["medium"]
    )
    rule8 = ctrl.Rule(
        degree_of_dirt["Medium"] | type_of_dirt["NonFat"], wash_time["short"]
    )
    rule9 = ctrl.Rule(
        degree_of_dirt["Low"] | type_of_dirt["NonFat"], wash_time["very_short"]
    )

    # Washing Control Simulation
    washing_ctrl = ctrl.ControlSystem(
        [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]
    )
    washing = ctrl.ControlSystemSimulation(washing_ctrl)


def fuzzify_laundry(fuzz_type, fuzz_degree):

    washing_machine.washing.input["type_of_dirt"] = fuzz_type
    washing_machine.washing.input["degree_of_dirt"] = fuzz_degree

    washing_machine.washing.compute()

    washing_machine.wash_time.view(sim=washing_machine.washing)
    plt.show()

    return washing_machine.washing.output["wash_time"]
