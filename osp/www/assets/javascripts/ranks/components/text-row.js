

import React, { Component, PropTypes } from 'react';

import Hit from './hit';
import Field from './field';


export default class extends Component {


  static propTypes = {
    hit: PropTypes.object.isRequired,
  };


  /**
   * Render a text row.
   */
  render() {

    this.hit = new Hit(this.props.hit);

    return (
      <tr className="text-row">

        <td className="rank">
          {this.hit.rank}
        </td>

        <td className="count">
          {this.hit.count}
        </td>

        <td className="count">
          {this.hit.score}
        </td>

        <td className="text">

          <a href={this.hit.path}>
            <div className="title" dangerouslySetInnerHTML={{
              __html: this.hit.field('title')
            }}></div>
          </a>

          <Field
            label="authors"
            value={this.hit.field('authors')}
          />

          <Field
            label="publisher"
            value={this.hit.field('publisher')}
          />

          <Field
            label="journal"
            value={this.hit.field('journal')}
          />

        </td>

      </tr>
    );

  }


}
