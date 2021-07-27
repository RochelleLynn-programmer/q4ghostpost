import React, { useState } from "react";
import axiosPath from "../../axios";
import "./Card.css";

function Card({ update, setUpdate, boast, content, downvotes, upvotes, id, secret, submitted }) {
  const [currentUpvotes, setCurrentUpvotes] = useState(upvotes);
  const [currentDownvotes, setCurrentDownvotes] = useState(downvotes);

  const upvote = (id) => {
    axiosPath
      .post(`${id}/upvote/`)
      .then((res) => {
        setUpdate(update + 1);
        setCurrentUpvotes(res.data.upvotes);
      })
      .catch((err) => console.log(err));
  };

  const downvote = (id) => {
    axiosPath
      .post(`${id}/downvote/`)
      .then((res) => {
        setUpdate(update + 1);
        setCurrentDownvotes(res.data.downvotes);
      })
      .catch((err) => console.log(err));
    setUpdate(update + 1);
  };

  return (
    <div className="card__card">
      {(() => {
        if (boast === true) {
          return <h2>This is a Boast</h2>;
        } else {
          return <h2>This is a Roast</h2>;
        }
      })()}

      <p>
        <b>Content:</b> {content}
      </p>
      <p>
        <b>Upvotes:</b> {currentUpvotes}
      </p>
      <p>
        <b>Downvotes:</b> {currentDownvotes}
      </p>
      <p>
        <b>Ranked:</b> {currentUpvotes - currentDownvotes}
      </p>
      <p>
        <b>Date Submitted:</b> {submitted}
      </p>
      <button onClick={() => upvote(id)}>Upvote</button>
      <button onClick={() => downvote(id)}>Downvote</button>
    </div>
  );
}

export default Card;
