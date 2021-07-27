import React from "react";
import axiosPath from "../../axios";
import Card from "../card/Card";
import { useState, useEffect } from "react";
import "./Main.css";

function Main() {
  const [data, setData] = useState([]);
  const [update, setUpdate] = useState(0);

  useEffect(() => {
    axiosPath.get().then((res) => setData(res.data));
  }, [update]);
  console.log(data);
  console.log(update);

  return (
    <div className="card_contain">
      {data.map(({ boast, content, downvotes, upvotes, id, secret, submitted }) => {
        return (
          <Card
            update={update}
            setUpdate={setUpdate}
            boast={boast}
            content={content}
            downvotes={downvotes}
            upvotes={upvotes}
            id={id}
            secret={secret}
            submitted={submitted}
            key={id}
          />
        );
      })}
    </div>
  );
}

export default Main;
