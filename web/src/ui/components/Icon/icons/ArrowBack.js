import React from 'react';
import { Icon } from '../Icon';

export function ArrowBack(props) {
  return (
    <Icon {...props} viewBox="0 0 24 24">
      <path d="M0 0h24v24H0z" fill="none" />
      <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" />
    </Icon>
  );
}

ArrowBack.defaultProps = Icon.defaultProps;

ArrowBack.propTypes = Icon.propTypes;
