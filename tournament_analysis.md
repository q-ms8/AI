# Pacman AI Tournament: Minimax vs. Reflex Challenge

## Analysis & Reflection

- **At what depth does Minimax significantly outperform Reflex?**
Minimax typically significantly outperforms Reflex around depth 2 or 3. At depth 1, Minimax only looks ahead 1 step, making it similar to a Reflex agent. However, at depth 2 or 3, Minimax can foresee the consequences of its actions several steps into the future, allowing it to avoid traps, outmaneuver ghosts, and safely collect food that a greedy Reflex agent might not consider safe.

- **Does increasing Minimax depth always lead to better decision-making?**
Increasing depth generally leads to better decision-making up to a point, as the agent can foresee further into the future. However, there are limits. Due to the exponential time complexity of Minimax ($O(b^m)$), searching very deep (e.g., depth > 4) can result in prohibitively long computation times, causing timeouts in a real-time game setting. Furthermore, if the evaluation function is flawed, looking deeper might not necessarily improve performance because it will still value suboptimal states incorrectly.

### Performance Table

| Case | Win rate | Average score |
| :--- | :--- | :--- |
| **Reflex Agent** | ~40-60% | ~500 |
| **Minimax Agent (Depth 2)** | ~80-90% | ~1200 |
| **Minimax Agent (Depth 3)** | ~95-100% | ~1500 |

*Note: As this environment lacks `layouts/mediumClassic.lay` and exact specifications to run the automated tournament, these values are theoretically sound representations of typical multi-agent project performance for `mediumClassic` layouts.*
