import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import utm

# set the app's title
st.title("SBET Reader")

sbet_f = st.file_uploader("SBET Solution File")
if sbet_f is not None:
    # Parse the file
    bytes_data = sbet_f.getvalue()

    sbet = np.frombuffer(bytes_data,dtype=np.float64).reshape((-1,17))
    
    st.subheader("Position")
    latlng = utm.from_latlon(sbet[:,1]*180.0/np.pi,sbet[:,2]*180.0/np.pi)
    fig, ax = plt.subplots()
    ax.plot(latlng[0],latlng[1])
    ax.set_xlabel('Easting [m]')
    ax.set_ylabel('Northing [m]')
    ax.ticklabel_format(useOffset=False,style='plain')
    st.pyplot(fig)

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


smrmsg_f = st.file_uploader("SMRMSG Solution Accuracy File")
if smrmsg_f is not None:
    # Parse the file
    bytes_data = smrmsg_f.getvalue()

    smrmsg = np.frombuffer(bytes_data,dtype=np.float64).reshape((-1,10))

    st.subheader("Position RMS Error")
    fig, ax = plt.subplots()
    line1, = ax.plot(smrmsg[:,0],smrmsg[:,1],'r-',label='North')
    line2, = ax.plot(smrmsg[:,0],smrmsg[:,2],'b-',label='East')
    line3, = ax.plot(smrmsg[:,0],smrmsg[:,3],'g-',label='Down')
    ax.set_ylabel('Position RMS Error [m]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)

    st.subheader("Velocity RMS Error")
    fig, ax = plt.subplots()
    line1, = ax.plot(smrmsg[:,0],smrmsg[:,4],'r-',label='North')
    line2, = ax.plot(smrmsg[:,0],smrmsg[:,5],'b-',label='East')
    line3, = ax.plot(smrmsg[:,0],smrmsg[:,6],'g-',label='Down')
    ax.set_ylabel('Velocity RMS Error [m/s]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)

    st.subheader("Angular RMS Error")
    fig, ax = plt.subplots()
    line1, = ax.plot(smrmsg[:,0],smrmsg[:,7]*0.0166667,'r-',label='Roll')
    line2, = ax.plot(smrmsg[:,0],smrmsg[:,8]*0.0166667,'b-',label='Pitch')
    line3, = ax.plot(smrmsg[:,0],smrmsg[:,9]*0.0166667,'g-',label='Heading')
    ax.set_ylabel('Angular RMS Error [deg]')
    ax.set_xlabel('Time [s]')
    ax.legend(handles=[line1,line2,line3])
    st.pyplot(fig)