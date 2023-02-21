# Learnable Nonlinear Circuits

This github repository is for the paper at DATE'23 - Highly Bespoke Robust Printed Neuromorphic Circuits

cite as
```
Highly Bespoke Robust Printed Neuromorphic Circuits
Zhao, H.; Hefenbrock, M.;Yang, Z; Beigl, M.; Tahoori, M.
2023 Design, Automation & Test in Europe Conference & Exhibition (DATE), April 17-19, 2023, IEEE.
```

# Usage of the code

Multiple setups can be found in folder `./LNC/` and can be run by:

* test different training and learning strategies. For trainig strategy, we consider training for weights and nonlinear circuits simultanously (update both parameters in the same epoch) or alternatively (1 epoch for weights, 1 epoch for nonlinear circuits, ...). For learning strategy, we consider differernt learning flexibilities on net-, layer-, and neuron-level.

~~~
$ sh 1.2_command_pNN_strategy.sh
~~~

* training pNNs with variation, but here the variation is applied on auxilary parameter $\eta$, instead of on the circuit components $\omega$.

~~~
$ sh 2.2_command_pNN_variation.sh
~~~

* training pNNs with variation on the circuit components $\omega$.

~~~
$ sh 3.2_command_pNN_variation_circuit.sh
~~~

* training pNNs with same setup in paper.

~~~
$ sh 4.1_train_for_paper.py
~~~


# Other materials

In `./simulation/` you can find the information and data for simulation of nonlinear circuits as well as the establishment of the surrogate nonlinear circuit model.
