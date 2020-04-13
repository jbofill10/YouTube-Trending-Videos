from sklearn.cluster import KMeans
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def kmeans(df, categories):

    df.replace({'category_id': categories}, inplace=True)

    x = df[['comment_count', 'dislikes', 'views', 'likes']]
    y = df['category_id']

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    scalar = StandardScaler()

    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test)

    model = param_tune(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred)*100)


def param_tune(x, y):

    grid = GridSearchCV(KMeans(), param_grid={'n_clusters': range(1,75)}, cv=5, refit=True, verbose=100)

    grid.fit(x, y)

    return grid.best_estimator_
