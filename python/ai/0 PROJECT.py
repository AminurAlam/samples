### downloading dataset
!test -e youth-tobacco-survey || curl -sLO 'https://www.kaggle.com/api/v1/datasets/download/anshtanwar/youth-tobacco-survey'
!unzip -qo youth-tobacco-survey
!echo '3221a4e9aedc81d7a91520da1cf9c6737276f6f4214d1522c9980953d87f58aa  datafile.csv' | sha256sum -c

### importing libraries
import textwrap
import warnings
import pandas     as pd
import numpy      as np
import seaborn    as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.preprocessing   import LabelEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics         import mean_absolute_error, mean_squared_error, root_mean_squared_error, mean_squared_log_error, root_mean_squared_log_error, r2_score
from sklearn.pipeline        import make_pipeline

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, PoissonRegressor, QuantileRegressor
from sklearn.tree         import DecisionTreeRegressor
from sklearn.ensemble     import RandomForestRegressor, GradientBoostingRegressor

### data correction
data = pd.read_csv("datafile.csv")

keys = [
    "Median age of initiation of Cigarette (in years)",
    "Median age of initiation of Bidi (in years)",
    "Median age of initiation of smokeless tobacco (in years)"
]

data.drop(keys, axis=1, inplace=True)

key = "Bought Cigarette as individual sticks in past 30 days    (%)"
data.loc[32, key] = 35.2
data[key] = pd.to_numeric(data[key])

key = "Students who saw anyone using tobacco on mass media in past 30 days  (%)"
data.loc[41, key] = 63.4
data[key] = pd.to_numeric(data[key])
data_copy = data.copy()

### misc
save_file = False
warnings.filterwarnings("ignore")
plt.style.use("ggplot")
colors = {
    "Rural": "#8EBA42",
    "Urban": "#E24A33",
    "Total": "#348ABD",
    "red": "#E24A33",
    "green": "#8EBA42",
    "blue": "#348ABD",
}

class Fig:
    figcount: int = 0

    def __call__(self):
        self.figcount += 1
        return str(self.figcount).zfill(2) + ".svg"

svg = Fig()

def get_col(model: str) -> str:
    if model.startswith("LinearRegression") or model.startswith('Pipeline'):
        return '#d20f39' # red
    elif model.startswith("Ridge"):
        return '#179299' # teal
    elif model.startswith("Lasso"):
        return '#7287fd' # lavender
    elif model.startswith("ElasticNet"):
        return '#8839ef' # mauve
    elif model.startswith("PoissonRegressor"):
        return '#df8e1d' # yellow
    elif model.startswith("QuantileRegressor"):
        return '#fe640b' # peach
    elif model.startswith("DecisionTreeRegressor") or model.startswith("RandomForestRegressor"):
        return '#40a02b' # green
    elif model.startswith("GradientBoostingRegressor"):
        return '#4c4f69' # grey
    return '#000000'
xattrs = [
    "Awareness about e-cigarette (%)",
    "Exposure to tobacco smoke at any outdoor public places  (%)",
    "Exposure to tobacco smoke at home   (%)",
    "Exposure to tobacco smoke at home/public place (%)",
    "Exposure to tobacco smoke inside any enclosed public  places  (%)",
    "Major source of tobacco product- Bidi: Paan shop (%)",
    "Major source of tobacco product- Bidi: Store   (%)",
    "Major source of tobacco product- Cigarette: Paan shop (%)",
    "Major source of tobacco product- Cigarette: Store   (%)",
    "Major source of tobacco product- Smokeless tobacco: Paan shop  (%)",
    "Major source of tobacco product- Smokeless tobacco: Store   (%)",
    "Refused sale of bidi because of age in past 30 days   (%)",
    "Refused sale of cigarette because of age in past 30 days   (%)",
    "Refused sale of smokeless tobacco because of age in past 30 days    (%)",
    "School heads aware of COTPA, 2003  (%)",
    "Schools authorized by the state government to collect fine for violation under Section-6 of the COTPA, 2003  (%)",
    "Schools aware of the policy for displaying ‘tobacco-free school’ board  (%)",
    "Schools followed ‘tobacco-free school’ guidelines  (%)",
    "Students who favoured ban on smoking at outdoor public places (%)",
    "Students who favoured ban on smoking inside enclosed public places (%)",
    "Students who noticed anti-tobacco messages anywhere in past 30 days    (%)",
    "Students who noticed anti-tobacco messages at sporting,  fairs, concerts, community events or social gatherings in past 30 days   (%)",
    "Students who noticed anti-tobacco messages in mass media in past 30 days    (%)",
    "Students who noticed cigarette advertisements/promotions at point of sale in past 30 days (%)",
    "Students who noticed health warnings on any tobacco product/cigarette packages in past 30 days       (%)",
    "Students who saw anyone smoking inside the  school building or outside school property (%)",
    "Students who saw anyone using tobacco on mass media in past 30 days  (%)",
    "Students who saw tobacco advertisements anywhere in past 30 days  (%)",
    "Students who thought it is difficult to quit once someone starts smoking tobacco (%)",
    "Students who thought other people’s tobacco smoking is harmful to them (%)",
    "Students who were taught in class about harmful effects of tobacco use during past 12 months (%)",
]
yattrs = [
    "Bought Bidi as individual sticks in past 30 days     (%)",
    "Bought Cigarette as individual sticks in past 30 days    (%)",
    "Current  smokeless tobacco users who wanted to quit tobacco now     (%)",
    "Current bidi smokers who bought bidi from a store, paan shop, or street vendor (%)",
    "Current bidi users (%)",
    "Current cigarette smokers who bought cigarettes from a store, paan shop, street vendor, or vending machine       (%)",
    "Current cigarette users (%)",
    "Current smokeless tobacco users (%)",
    "Current smokeless tobacco users who tried to quit tobacco in the past 12 months   (%)",
    "Current tobacco smokers (%)",
    "Current tobacco smokers who tried to quit smoking in the past 12 months (%)",
    "Current tobacco smokers who wanted to quit smoking now   (%)",
    "Current tobacco users (%)",
    "Ever  smokeless tobacco users who quit  in last 12 months (%)",
    "Ever bidi users (%) ",
    "Ever cigarette users (%)",
    "Ever e-cigarette use (%)",
    "Ever smokeless tobacco users (%)",
    "Ever tobacco smokers (%)",
    "Ever tobacco smokers who quit in last 12 months (%)",
    "Ever tobacco users (%)",
    "Ever users of  paan masala together with tobacco (%)",
    "Never cigarette smokers susceptible to cigarette use in future (%)",
]
# toplists
for title, key in {
    "that ever used tobacco": "Ever tobacco users (%)",
    "that are currently using tobacco": "Current tobacco users (%)",
    "with most quitters": "Ever tobacco smokers who quit in last 12 months (%)",
    "who want to quit": "Current tobacco smokers who wanted to quit smoking now   (%)",
}.items():
    top = data_copy.nlargest(10, key)
    plt.figure(figsize=(10, 6))
    plt.barh(top["State/UT"] + " " + top["Area"], top[key], color=list(map(lambda x: colors[x], top["Area"])))
    plt.xlabel(key)
    plt.title("Top 10 states " + title)
    plt.gca().invert_yaxis()
    plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# source of tobacco
for title, categories in {
    "All time popular sources": [
        "Ever tobacco users (%)",
        "Ever smokeless tobacco users (%)",
        "Ever tobacco smokers (%)",
        "Ever cigarette users (%)",
        "Ever users of  paan masala together with tobacco (%)",
        "Ever bidi users (%) ",
        "Ever e-cigarette use (%)",
    ],
    "Current popular sources": [
        "Current tobacco users (%)",
        "Current tobacco smokers (%)",
        "Current smokeless tobacco users (%)",
        'Current cigarette users (%)',
        'Current bidi users (%)',
    ],
    "Shops for tobacco": [
        "Major source of tobacco product- Bidi: Store   (%)",
        "Major source of tobacco product- Smokeless tobacco: Store   (%)",
        "Major source of tobacco product- Cigarette: Store   (%)",
        "Major source of tobacco product- Bidi: Paan shop (%)",
        "Major source of tobacco product- Cigarette: Paan shop (%)",
        "Major source of tobacco product- Smokeless tobacco: Paan shop  (%)",
]}.items():
    plt.figure(figsize=(10, 6))
    plt.barh(categories, [data_copy.iloc[0][key] for key in categories], color=colors['blue'])
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# data distribution
for index in range(3):
    fig, ax = plt.subplots(figsize=(18,8))
    attrs = data[data_copy['Area'] == 'Total'][data_copy.columns[(index*18) + 2:((index+1)*18)+2]]

    for attr in attrs:
        #print(attrs[attr])
        mean = attrs[attr].mean()
        min_max = [[mean - attrs[attr].min()], [attrs[attr].max() - mean]]
        #print(attr, min_max)
        ax.errorbar(attr, mean, yerr=min_max, fmt='o', color=colors['blue'], capsize=4)

    ax.set_xticks(
        attrs.columns,
        labels=['\n'.join(textwrap.wrap(i[:-4], width=30)) for i in attrs],
        rotation=60,
        rotation_mode='anchor',
        ha='right'
    )
    ax.set(title=f"Highest, Lowest and Mean values of columns (Part {index+1})", ylabel="percentage (%)")
    plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# correlation between some columns
for a, b in [
  ("Students who noticed anti-tobacco messages anywhere in past 30 days    (%)","Current tobacco smokers who tried to quit smoking in the past 12 months (%)"),
  ("Schools followed ‘tobacco-free school’ guidelines  (%)", "Current tobacco users (%)"),
  ("Awareness about e-cigarette (%)", "Ever e-cigarette use (%)"),
  ("Exposure to tobacco smoke at home/public place (%)", "Current cigarette users (%)"),
]:
  X, y = data_copy[[a]], data_copy[b]

  model = LinearRegression()
  model.fit(X, y)

  plt.figure(figsize=(8, 6))
  plt.scatter(X, y, color=colors['blue'], alpha=0.6, label="States")
  plt.plot(X, model.predict(X), color=colors['red'], linewidth=2, label="Regression Line")
  plt.xlabel(textwrap.shorten(a, width=70, placeholder='…'))
  plt.ylabel(textwrap.shorten(b, width=50, placeholder='…'))
  plt.title(f"{a}\nVS\n{b}")
  plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# correlation table
display(round(data_copy.drop(['State/UT', 'Area'], axis=1).corr().head(), 2))

# covariance table
display(round(data_copy.drop(['State/UT', 'Area'], axis=1).cov().head(), 2))
# corr & cov as heatmaps
vars = [
    "Awareness about e-cigarette (%)",
    "Exposure to tobacco smoke at home/public place (%)",
    "Refused sale of bidi because of age in past 30 days   (%)",
    "Refused sale of cigarette because of age in past 30 days   (%)",
    "Refused sale of smokeless tobacco because of age in past 30 days    (%)",
    "Schools followed ‘tobacco-free school’ guidelines  (%)",
    "Students who noticed anti-tobacco messages anywhere in past 30 days    (%)",
    "Students who saw anyone using tobacco on mass media in past 30 days  (%)",
    "Students who saw tobacco advertisements anywhere in past 30 days  (%)",
    "Students who thought it is difficult to quit once someone starts smoking tobacco (%)",
    "Students who thought other people’s tobacco smoking is harmful to them (%)",
    "Students who were taught in class about harmful effects of tobacco use during past 12 months (%)",

    "Current bidi users (%)",
    "Current cigarette users (%)",
    "Current tobacco users (%)",
    "Ever  smokeless tobacco users who quit  in last 12 months (%)",
    "Ever tobacco users (%)",
    "Never cigarette smokers susceptible to cigarette use in future (%)",
]

labelmod = lambda tks, l: list(map(
    lambda T: textwrap.shorten(T._text[:-4], width=l, placeholder='…'), tks
))
params = mpl.rcParams
style = sns.axes_style()
sns.set_theme(style='dark')

corr_matrix = data_copy[vars].corr()
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, cmap="coolwarm", linewidths=0.2, mask=np.triu(np.ones_like(corr_matrix, dtype=bool)))
plt.title("Correlation Heatmap")
ax.set_yticklabels(labelmod(ax.get_yticklabels(), 50))
ax.set_xticklabels(labelmod(ax.get_xticklabels(), 30), rotation=45, ha='right')
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

cov_matrix = data_copy[vars].cov()
fig, ax = plt.subplots()
sns.heatmap(cov_matrix, cmap="coolwarm", linewidths=0.2, mask=np.triu(np.ones_like(cov_matrix, dtype=bool)))
plt.title("Coavariance Heatmap")
ax.set_yticklabels(labelmod(ax.get_yticklabels(), 50))
ax.set_xticklabels(labelmod(ax.get_xticklabels(), 30), rotation=45, ha='right')
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

sns.set_theme(style=style)
mpl.rcParams = params
plt.style.use("ggplot")
# data cleanup

data = data[data['Area'] == 'Total']
data = data.drop('Area', axis=1)
data = data.iloc[1:]

data.reset_index(drop=True, inplace=True)


### label encoding example
le = LabelEncoder()
data['State/UT'] = le.fit_transform(data['State/UT'])

### train test split
xtr, xts, ytr, yts = train_test_split(data[xattrs], data[["Ever tobacco smokers who quit in last 12 months (%)"]], test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(xtr, ytr)
coef = model.coef_[0]

positive_attrs = sorted(
    list(filter(lambda x: x[0] > 0, zip(coef, xattrs))),
    key=lambda item: item[0], reverse=True)
negative_attrs = sorted(
    list(filter(lambda x: x[0] < 0, zip(coef, xattrs))),
    key=lambda item: item[0])

plt.figure(figsize=(18, 9))
plt.bar(
    [i[1] for i in positive_attrs],
    [i[0] for i in positive_attrs],
    color=colors['green'])
plt.xticks(
    range(len(positive_attrs)),
    ['\n'.join(textwrap.wrap(i[1][:-4], width=30)) for i in positive_attrs],
    rotation=60,
    rotation_mode='anchor',
    ha='right'
)
plt.xlabel("Attributes")
plt.ylabel("Coefficient")
plt.title("Attributes for people who quit smoking")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

plt.figure(figsize=(18, 9))
plt.bar(
    [i[1] for i in negative_attrs],
    [-i[0] for i in negative_attrs],
    color=colors['red'])
plt.xticks(
    range(len(negative_attrs)),
    ['\n'.join(textwrap.wrap(i[1][:-4], width=30)) for i in negative_attrs],
    rotation=60,
    rotation_mode='anchor',
    ha='right'
)
plt.xlabel("Attributes")
plt.ylabel("Coefficient")
plt.title("Attributes for people who didnt quit smoking")
plt.tight_layout()
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
scores = []
for model in [
    LinearRegression(),
    make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
    Ridge(random_state=0),
    Lasso(random_state=0),
    ElasticNet(random_state=0),
    #PoissonRegressor(),
    QuantileRegressor(),
    DecisionTreeRegressor(random_state=0),
    RandomForestRegressor(random_state=0),
    GradientBoostingRegressor(random_state=0),
]:
    model.fit(xtr, ytr)
    pred = model.predict(xts)
    scores.append([
        model.__class__.__name__,
        r2_score(yts, pred),
        mean_absolute_error(yts, pred),
    ])
scores = sorted(scores, key=lambda item: item[1])
highest = max([i[1] for i in scores])
lowest = min([i[1] for i in scores])

plt.figure(figsize=(10, 6))
for score in scores:
    plt.barh(score[0], (score[1] - lowest)/(highest-lowest))
plt.xlabel(f"Score (normalized)")
plt.title("R² Score (Higher is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

plt.figure(figsize=(10, 6))
for score in scores:
    plt.barh(score[0], score[2])
plt.xlabel("Error")
plt.title("Mean Absolute Error (Lower is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
degrees = range(2, 7)
err = []

for d in degrees:
    pipe = make_pipeline(PolynomialFeatures(degree=d), LinearRegression())
    pipe.fit(xtr, ytr)
    err.append(mean_absolute_error(yts, pipe.predict(xts)))

min_err = min(err)
best_alpha = degrees[err.index(min_err)]

plt.figure(figsize=(10, 6))
plt.plot(degrees, err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title("LinearRegression with preprocessing")
plt.xlabel("degree of PolynomialFeatures")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")
solvers = ['svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga' ]
s_err = []

for s in solvers:
    alphas = np.arange(200)
    a_err = []

    for a in alphas:
        model = Ridge(alpha=a, solver=s)
        model.fit(xtr, ytr)
        a_err.append(mean_absolute_error(yts, model.predict(xts)))

    min_err = min(a_err)
    best_alpha = alphas[a_err.index(min_err)]

    plt.figure(figsize=(10, 6))
    plt.plot(alphas, a_err)
    plt.scatter(best_alpha, min_err, color=colors['blue'])
    plt.title(f"{s} solver")
    plt.xlabel("alpha")
    plt.ylabel("error")
    plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

    print(f"best value of alpha for {s} is {best_alpha}")
    s_err.append(best_alpha)

min_err = min(s_err)
best_solver = alphas[s_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.barh(solvers, s_err)
plt.barh(best_solver, min_err, color=colors['blue'])
plt.title("Solver ranking")
plt.xlabel("best alpha")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
solvers = ['svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']
alphas = np.arange(5, 100)

x_grid, y_grid = np.meshgrid(alphas, solvers)
errors = np.zeros_like(x_grid, dtype=float)

for i, s in enumerate(solvers):
    for j, a in enumerate(alphas):
        model = Ridge(alpha=a, solver=s)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')

surf = ax.plot_surface(x_grid, np.arange(len(solvers))[:, None], errors, cmap='viridis')
ax.set_xticks(np.arange(0, 100, 25))
ax.set_yticks(np.arange(len(solvers)), labels=solvers)
ax.set(xlabel='Alpha', ylabel='Solver', zlabel='Mean Absolute Error', zlim=(errors.min(), errors.max()+0.5))
fig.colorbar(surf)
plt.title("Ridge on different alpha values and solvers")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
alphas = np.arange(100)
a_err = []

for a in alphas:
    model = Lasso(alpha=a)
    model.fit(xtr, ytr)
    a_err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(a_err)
best_alpha = alphas[a_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(alphas, a_err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title("Lasso on different alpha")
plt.xlabel("alpha")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")
alphas = np.arange(200)
a_err = []

for a in alphas:
    model = ElasticNet(alpha=a)
    model.fit(xtr, ytr)
    a_err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(a_err)
best_alpha = alphas[a_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(alphas, a_err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title(f"ElasticNet on different alpha")
plt.xlabel("alpha")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")
ratios = np.arange(0.1, 1.0, 0.05)
alphas = np.arange(2, 100, 2)
min_err = 100
min_pos = [0,0]

x_grid, y_grid = np.meshgrid(alphas, ratios)
errors = np.zeros_like(x_grid, dtype=float)

for i, l in enumerate(ratios):
    for j, a in enumerate(alphas):
        model = ElasticNet(alpha=a, l1_ratio=l)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))
        if errors[i, j] < min_err:
            min_err = errors[i, j]
            min_pos = [i, j]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')

surf = ax.plot_surface(x_grid, y_grid, errors, cmap='viridis')
ax.set(xlabel='Alpha', ylabel='L1 Ratio', zlabel='Mean Absolute Error', zlim=(8, 20))
fig.colorbar(surf)
plt.title("ElasticNet on different alpha and L1 ratio values")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {alphas[min_pos[1]]}")
print(f"best value of l1_ratio is ~{ratios[min_pos[0]]:.2f}")
alphas = np.arange(1_000, 100_000, 5_000)
a_err = []

for a in alphas:
    model = PoissonRegressor(alpha=a)
    model.fit(xtr, ytr)
    a_err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(a_err)
best_alpha = alphas[a_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(alphas, a_err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title("Poisson on different alpha")
plt.xlabel("alpha")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")

alphas = np.arange(36_400, 36_600, 10)
a_err = []

for a in alphas:
    model = PoissonRegressor(alpha=a)
    model.fit(xtr, ytr)
    a_err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(a_err)
best_alpha = alphas[a_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(alphas, a_err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title("Poisson on different alpha (Zoomed In)")
plt.xlabel("alpha")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")
alphas = np.arange(100)/10
a_err = []

for a in alphas:
    model = QuantileRegressor(alpha=a)
    model.fit(xtr, ytr)
    a_err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(a_err)
best_alpha = alphas[a_err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(alphas, a_err)
plt.scatter(best_alpha, min_err, color=colors['blue'])
plt.title("QuantileRegressor on different alpha values")
plt.xlabel("alpha")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_alpha}")
alphas = np.arange(0.1, 5, 0.1)
quantiles = np.arange(0.2, 0.90, 0.03)
min_err = 100
min_pos = [0,0]

x_grid, y_grid = np.meshgrid(alphas, quantiles)
errors = np.zeros_like(x_grid, dtype=float)

for i, q in enumerate(quantiles):
    for j, a in enumerate(alphas):
        model = QuantileRegressor(alpha=a, quantile=q)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))
        if errors[i, j] < min_err:
            min_err = errors[i, j]
            min_pos = [i, j]
best_x = alphas[min_pos[1]]
best_y = quantiles[min_pos[0]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')
surf = ax.plot_surface(x_grid, y_grid, errors, cmap='viridis')
ax.set(xlabel='Alpha', ylabel='Quantile', zlabel='Mean Absolute Error', zlim=(2, 28))
fig.colorbar(surf)
plt.title("QuantileRegressor on different alpha and quantile values")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of alpha is {best_x:.2f}")
print(f"best value of quantile is ~{best_y:.2f}")
splits = np.arange(2, 150, 1)
err = []

for s in splits:
    model = DecisionTreeRegressor(min_samples_split=s)
    model.fit(xtr, ytr)
    err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(err)
best_split = splits[err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(splits, err)
plt.scatter(best_split, min_err, color=colors['blue'])
plt.title(f"DecisionTree at different splits")
plt.xlabel("minimun sample split")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best size of min_sample_split is {best_split}")
splits = np.arange(2, 60, 3)
depths = np.arange(1, 100, 4)
min_err = 100
min_pos = [0,0]

x_grid, y_grid = np.meshgrid(splits, depths)
errors = np.zeros_like(x_grid, dtype=float)

for i, d in enumerate(depths):
    for j, s in enumerate(splits):
        model = DecisionTreeRegressor(min_samples_split=s, max_depth=d)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))
        if errors[i, j] < min_err:
            min_err = errors[i, j]
            min_pos = [i, j]

best_x = splits[min_pos[1]]
best_y = depths[min_pos[0]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')
surf = ax.plot_surface(x_grid, y_grid, errors, cmap='viridis')
ax.set(xlabel='Splits', ylabel='Max Depth', zlabel='Mean Absolute Error', zlim=(errors.min(), errors.max()+10))
fig.colorbar(surf)
plt.title("Decision Tree on different splits and depths")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best value of split is {best_x}")
print(f"best value of depth is {best_y}")
estimators = np.arange(10, 200, 10)
err = []

for d in estimators:
    model = RandomForestRegressor(random_state=0, n_estimators=d)
    model.fit(xtr, ytr)
    err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(err)
best = estimators[err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(estimators, err)
plt.scatter(best, min_err, color=colors['blue'])
plt.title("Random Forest at different estimators")
plt.xlabel("number of estimators")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best number of estimator is {best}")
estimators = np.arange(70, 130, 5)
splits = np.arange(2, 20, 1)
min_err = 100
min_pos = [0,0]

x_grid, y_grid = np.meshgrid(estimators, splits)
errors = np.zeros_like(x_grid, dtype=float)

for i, s in enumerate(splits):
    for j, e in enumerate(estimators):
        model = RandomForestRegressor(random_state=0, n_estimators=e, min_samples_split=s)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))
        if errors[i, j] < min_err:
            min_err = errors[i, j]
            min_pos = [i, j]

best_x = estimators[min_pos[1]]
best_y = splits[min_pos[0]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')
surf = ax.plot_surface(x_grid, y_grid, errors, cmap='viridis')
ax.set(xlabel='Number of Entimators', ylabel='Splits', zlabel='Mean Absolute Error', zlim=(errors.min(), errors.max()+1.5))
fig.colorbar(surf)
plt.title("Random Forest on different estimators and splits")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best number of estimators is {best_x}")
print(f"best minimum sample splits is {best_y}")
rates = np.arange(0, 1, 0.05)
err = []

for r in rates:
    model = GradientBoostingRegressor(learning_rate=r)
    model.fit(xtr, ytr)
    err.append(mean_absolute_error(yts, model.predict(xts)))

min_err = min(err)
best = rates[err.index(min_err)]

plt.figure(figsize=(10,6))
plt.plot(rates, err)
plt.scatter(best, min_err, color=colors['blue'])
plt.title("Gradient Boosting at different learning rates")
plt.xlabel("learning rate")
plt.ylabel("error")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best learning rate is {best}")
rates = np.arange(0, 1, 0.05)
estimators = np.arange(1, 40, 2)
min_err = 100
min_pos = [0,0]

x_grid, y_grid = np.meshgrid(rates, estimators)
errors = np.zeros_like(x_grid, dtype=float)

for i, e in enumerate(estimators):
    for j, r in enumerate(rates):
        model = GradientBoostingRegressor(learning_rate=r, n_estimators=e)
        model.fit(xtr, ytr)
        errors[i, j] = mean_absolute_error(yts, model.predict(xts))
        if errors[i, j] < min_err:
            min_err = errors[i, j]
            min_pos = [i, j]

best_x = rates[min_pos[1]]
best_y = estimators[min_pos[0]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(projection='3d', facecolor='#fff')
surf = ax.plot_surface(x_grid, y_grid, errors, cmap='viridis')
ax.set(xlabel='Rate', ylabel='Number of Estimators', zlabel='Mean Absolute Error', zlim=(errors.min(), errors.max()+13))
fig.colorbar(surf)
plt.title("Gradient Boosting on different learning rates and estimators")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")

print(f"best learning rate is {best_x}")
print(f"best number of estimators is {best_y}")
# me
err = dict()
for model in [
    make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
    Ridge(alpha=2),
    Lasso(alpha=2),
    ElasticNet(alpha=2, l1_ratio=0.5),
    PoissonRegressor(alpha=200),
    QuantileRegressor(alpha=5, quantile=0.5),
    DecisionTreeRegressor(min_samples_split=10, max_depth=2),
    RandomForestRegressor(random_state=0),
    GradientBoostingRegressor(random_state=0, learning_rate=1, n_estimators=5),
]:
    model.fit(xtr, ytr)
    err[str(model)] = mean_absolute_error(yts, model.predict(xts))

plt.figure(figsize=(10, 6))
for m in sorted(err, key=err.get, reverse=True):
    plt.barh(m
        .replace(', random_state=0', '')
        .replace('random_state=0', '')
        .replace('Regressor', '')
        .replace("(steps=[('polynomialfeatures', PolynomialFeatures(", '(')
        .replace(")),\n                ('linearregression', LinearRegression())])", ')'),
        err[m], color=get_col(m))
plt.xlabel("Error")
plt.title("Mean Absolute Error (Lower is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# me
err = dict()
for model in [
    make_pipeline(PolynomialFeatures(degree=5), LinearRegression()),
    Ridge(alpha=50, solver='auto'),
    Lasso(alpha=33.0),
    ElasticNet(alpha=14, l1_ratio=0.44),
    PoissonRegressor(alpha=36480),
    QuantileRegressor(alpha=1.2, quantile=0.46),
    DecisionTreeRegressor(min_samples_split=29, max_depth=1),
    RandomForestRegressor(random_state=0, n_estimators=100, min_samples_split=11),
    GradientBoostingRegressor(learning_rate=0, n_estimators=1),
]:
    model.fit(xtr, ytr)
    err[str(model)] = mean_absolute_error(yts, model.predict(xts))

plt.figure(figsize=(10,6))
for m in sorted(err, key=err.get, reverse=True):
    plt.barh(m
        .replace(', random_state=0', '')
        .replace('Regressor', '')
        .replace("(steps=[('polynomialfeatures', PolynomialFeatures(", '(')
        .replace(")),\n                ('linearregression', LinearRegression())])", ')'),
        err[m], color=get_col(m))
plt.xlabel("Error")
plt.title("Mean Absolute Error (Lower is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# mse
err = dict()
for model in [
    make_pipeline(PolynomialFeatures(degree=5), LinearRegression()),
    Ridge(alpha=50, solver='auto'),
    Lasso(alpha=33.0),
    ElasticNet(alpha=14, l1_ratio=0.44),
    PoissonRegressor(alpha=36480),
    QuantileRegressor(alpha=1.2, quantile=0.46),
    DecisionTreeRegressor(min_samples_split=29, max_depth=1),
    RandomForestRegressor(random_state=0, n_estimators=100, min_samples_split=11),
    GradientBoostingRegressor(learning_rate=0, n_estimators=1),
]:
    model.fit(xtr, ytr)
    err[str(model)] = mean_squared_error(yts, model.predict(xts))

plt.figure(figsize=(10,6))
for m in sorted(err, key=err.get, reverse=True):
    plt.barh(m
        .replace(', random_state=0', '')
        .replace('Regressor', '')
        .replace("(steps=[('polynomialfeatures', PolynomialFeatures(", '(')
        .replace(")),\n                ('linearregression', LinearRegression())])", ')'),
        err[m], color=get_col(m))
plt.xlabel("Error")
plt.title("Mean Squared Error (Lower is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# rmse
err = dict()
for model in [
    make_pipeline(PolynomialFeatures(degree=5), LinearRegression()),
    Ridge(alpha=50, solver='auto'),
    Lasso(alpha=33.0),
    ElasticNet(alpha=14, l1_ratio=0.44),
    PoissonRegressor(alpha=36480),
    QuantileRegressor(alpha=1.2, quantile=0.46),
    DecisionTreeRegressor(min_samples_split=29, max_depth=1),
    RandomForestRegressor(random_state=0, n_estimators=100, min_samples_split=11),
    GradientBoostingRegressor(learning_rate=0, n_estimators=1),
]:
    model.fit(xtr, ytr)
    err[str(model)] = root_mean_squared_error(yts, model.predict(xts))

plt.figure(figsize=(10,6))
for m in sorted(err, key=err.get, reverse=True):
    plt.barh(m
        .replace(', random_state=0', '')
        .replace('Regressor', '')
        .replace("(steps=[('polynomialfeatures', PolynomialFeatures(", '(')
        .replace(")),\n                ('linearregression', LinearRegression())])", ')'),
        err[m], color=get_col(m))
plt.xlabel("Error")
plt.title("Root Mean Squared Error (Lower is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
# R² error
err = dict()
for model in [
    make_pipeline(PolynomialFeatures(degree=5), LinearRegression()),
    Ridge(alpha=50, solver='auto'),
    Lasso(alpha=33.0),
    ElasticNet(alpha=14, l1_ratio=0.44),
    PoissonRegressor(alpha=36480),
    QuantileRegressor(alpha=1.2, quantile=0.46),
    DecisionTreeRegressor(min_samples_split=29, max_depth=1),
    RandomForestRegressor(random_state=0, n_estimators=100, min_samples_split=11),
    GradientBoostingRegressor(learning_rate=0, n_estimators=1),
]:
    model.fit(xtr, ytr)
    err[str(model)] = r2_score(yts, model.predict(xts))

plt.figure(figsize=(10,6))
for m in sorted(err, key=err.get, reverse=False):
    plt.barh(m
        .replace(', random_state=0', '')
        .replace('Regressor', '')
        .replace("(steps=[('polynomialfeatures', PolynomialFeatures(", '(')
        .replace(")),\n                ('linearregression', LinearRegression())])", ')'),
        err[m], color=get_col(m))
plt.xlabel("Error")
plt.title("R² Score (Higher is better)")
plt.show() if not save_file else plt.savefig(svg(), bbox_inches="tight")
if save_file:
    !rm svg.zip
    !zip --move svg.zip *.svg
