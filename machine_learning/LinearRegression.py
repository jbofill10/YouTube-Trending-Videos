from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

def run(df):
    X = df[['comment_count', 'dislikes', 'views', 'comments_disabled', 'ratings_disabled']]
    Y = df['likes']

    regular_linear_regression(X,Y)


def regular_linear_regression(x,y):
    scalar = StandardScaler()
    lin_regressor = LinearRegression()

    x_train, x_test, y_train, y_test = train_test_split(x,y)

    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test)
    lin_regressor.fit(x_train, y_train)
    y_pred = lin_regressor.predict(x_test)

    y_result = mean_squared_error(y_test, y_pred)
    
    print(y_result)