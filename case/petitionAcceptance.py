def petition_acceptance_metric(text_inp):
    """Function for petition acceptance prediction
        Input:
            text_inp -> (list of str) Input(petition content) of Type
            model_path -> (str) Filepath of trained sklearn model with '.joblib' extension
            predict_prob -> (Boolean) Default::True Outputs petition submission result(1 for acceptance, 0 for rejection),probability of prediction (if predict_prob set to True)
            vectorizer_path -> (str) Filepath of TFid vectorizer with '.pickle' extension
            
        Output:
            if predict_prob is True -> returns two numbers prediction(1 or 0),probability(float)
    """
    
    from joblib import load
    import pickle
    import pandas as pd

    model_path = 'Ridgeclassifier.joblib'
    vectorizer_path = 'vectorizer.pickle'
    
    text_inp = pd.DataFrame(text_inp,columns=['text'])
    
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    pred_vec = vectorizer.transform(text_inp)
    
    clf = load(model_path)  
    return clf.predict(pred_vec),clf.decision_function(pred_vec)



