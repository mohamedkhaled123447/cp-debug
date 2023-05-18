import React from 'react';
import { MDBRow, MDBCol, MDBInput } from 'mdb-react-ui-kit';

export default function App() {
  return (
    <>
      <div className="container mt-4">
      <MDBRow className='mb-3'>
          <MDBCol md='6'>
            <MDBInput type='textarea' label='Example textarea' rows='8' />
          </MDBCol>
          <MDBCol md='6'>
            <MDBInput type='textarea' label='Example textarea' rows='8' />
          </MDBCol>
        </MDBRow>
        <MDBRow className='mb-3'>
          <MDBCol>
            <MDBInput type='textarea' label='Example textarea' rows='8' />
          </MDBCol>
        </MDBRow>
        <MDBRow className='mb-3'>
          <MDBCol md='6'>
            <MDBInput type='textarea' label='Example textarea' rows='8' />
          </MDBCol>
          <MDBCol md='6'>
            <MDBInput type='textarea' label='Example textarea' rows='8' />
          </MDBCol>
        </MDBRow>
      </div>
    </>
  );
}