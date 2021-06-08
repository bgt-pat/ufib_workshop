def predict(x,u,A,B,P,Q):
    """
    Prediction step of the Kalman filter
    
    Input:
    x - state vector
    u - input vector
    A - process matrix
    B - input-to-state matrix
    P - state covariance matrix
    Q - evolution noise
    
    Returns:
    x - predicted state
    P - predicted covariance
    """
    xpls = A.dot(x) + B.dot(u)
    P = A.dot(P).dot(A.T) + Q
    return xpls, P

def update(y,xpls,C,P,R):
    """
    Update step of the Kalman filter
    
    Input:
    y - measurement
    xpls - predicted state
    C - measurement matrix
    P - covariance matrix
    R - measurement noise
    
    Returns:
    x - updated step after measurement
    P - updated covariance
    K - Kalman gain
    """

    K = P.dot(C.T).dot(np.linalg.pinv(C.dot(P).dot(C.T) + R))
    # Update estimate via measurement
    x = xpls + K.dot(y - C.dot(xpls))
    # Update error covariance
    P = P - K.dot(C).dot(P)
    return x, P, K