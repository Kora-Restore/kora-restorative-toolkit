# 📊 Kōra Dataset: Historical Civilization Inputs (Ancient Era)

This dataset contains input variables used to calculate the Peace & Wellbeing Index (PWI) for ancient civilizations.  
The dataset is simplified for demonstration and model testing purposes.

---

## ⚖️ Variables Explained

| Variable                | Meaning                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `Civilization`           | Name of the society or empire                                           |
| `Conflicts_per_century`  | Average number of external or internal wars per 100 years               |
| `Deaths_per_conflict`    | Estimated average deaths per major conflict (rounded for simplicity)    |
| `BHW` (Basic Human Wellbeing) | Estimate of life expectancy, food access, housing, health, and safety |
| `EF` (Equality & Fairness)     | Estimate of class hierarchy, gender equity, slave presence, legal parity |
| `ES` (Ecological Sustainability) | Approximate relationship to land, ecological impact, resource use       |

All values are normalized on a scale of 0 to 100.

---

## 📚 How These Numbers Were Created

These estimates were based on a combination of:

1. **Historical scholarship**
   - Sources like "The Human Web" (J.R. & William McNeill), "Guns, Germs & Steel" (Diamond), and World History Atlas.
   - Peer-reviewed articles, UNESCO records, and archaeological summaries

2. **Pattern logic**
   - Civilizations with empire-building, slavery, and colonialism typically had lower EF scores
   - Societies with sustainable agriculture and low warfare scored higher on ES
   - High warfare and elite dominance = higher conflict + lower wellbeing

3. **Simplified rounding for clarity**
   - All numbers are **heuristic**: they are proxies meant to provoke comparison and evolve over time.
   - More precise scoring systems can emerge as contributors refine each metric or attach sources.

---

## 🧠 Example Notes (Line-by-Line)

### ✅ Maya Civilization
- Known for advanced science, engineering, and sustainable agroforestry in early periods
- Internal warfare common but low-scale early on → **2 conflicts per century**, **~1000 deaths**
- High ecological harmony → ES = 90

### 🟡 Ancient Greece
- Frequent war between city-states (e.g. Peloponnesian Wars) → 10 conflicts per century
- High intellectual development, but slavery, exclusion of women → low EF
- Deforestation and marble mining → ES = 45

### 🔴 Ancient Rome
- Near-constant war and expansion → 12+ conflicts per century
- Enslavement, extreme inequality → EF = 30
- High urbanization and environmental degradation → ES = 40

---

## ⚠️ Limitations

- This is not an academic index (yet).
- These numbers are starting points for **open discussion, transparency, and refinement.**
- **Regional experts, historians, and communities are invited** to refine, debate, and improve them.

---

## 🧭 Next Goals

- Attach each row to at least 1 supporting citation or dataset
- Build a `sources.md` or a `references/` folder
- Allow alternate scoring systems (e.g. low–medium–high scales, confidence intervals)

---

> 📣 Want to improve this dataset?
> Open a pull request, suggest edits in a discussion, or fork the repo for regional adaptations.
