
import numpy as np

# ... your other code ...

features = np.array([[area, bedrooms, bathrooms, stories, 
                      1 if mainroad=="yes" else 0, 
                      1 if guestroom=="yes" else 0, 
                      1 if basement=="yes" else 0, 
                      0, 1 if airconditioning=="yes" else 0, 
                      parking, 0, 1]])

prediction = model.predict(features)
print(prediction[0])
