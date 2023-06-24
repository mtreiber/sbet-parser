import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# set the app's title
st.title("SBET Reader")

sbet_f = st.file_uploader("SBET File")
if sbet_f is not None:
    # Parse the file
    bytes_data = sbet_f.getvalue()

    sbet = np.frombuffer(bytes_data,dtype=np.float64).reshape((-1,17))

    st.subheader("Altitude")
    fig, ax = plt.subplots()
    ax.plot(sbet[:,0],sbet[:,3])
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Altitude [m]')
    st.pyplot(fig)

    st.subheader("Orientation")
    fig, ax = plt.subplots()
    line1, = ax.plot(sbet[:,0],sbet[:,7]*180.0/np.pi,'r-',label='Roll')
    line2, = ax.plot(sbet[:,0],sbet[:,8]*180.0/np.pi,'b-',label='Pitch')
    line3, = ax.plot(sbet[:,0],sbet[:,9]*180.0/np.pi,'g-',label='Heading')
    ax.set_ylabel('Angle [deg]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)

    st.subheader("Velocity")
    fig, ax = plt.subplots()
    line1, = ax.plot(sbet[:,0],sbet[:,4],'r-',label='X')
    line2, = ax.plot(sbet[:,0],sbet[:,5],'b-',label='Y')
    line3, = ax.plot(sbet[:,0],sbet[:,6],'g-',label='Z')
    ax.set_ylabel('Velocity [m/s]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)

    st.subheader("Acceleration")
    fig, ax = plt.subplots()
    line1, = ax.plot(sbet[:,0],sbet[:,11],'r-',label='X')
    line2, = ax.plot(sbet[:,0],sbet[:,12],'b-',label='Y')
    line3, = ax.plot(sbet[:,0],sbet[:,13],'g-',label='Z')
    ax.set_ylabel('Acceleration [m/s2]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)

    st.subheader("Rotation Rates")
    fig, ax = plt.subplots()
    line1, = ax.plot(sbet[:,0],sbet[:,14]*180.0/np.pi,'r-',label='X')
    line2, = ax.plot(sbet[:,0],sbet[:,15]*180.0/np.pi,'b-',label='Y')
    line3, = ax.plot(sbet[:,0],sbet[:,16]*180.0/np.pi,'g-',label='Z')
    ax.set_ylabel('Angular Rate [deg/s]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)