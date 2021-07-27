import React from "react";
import { useForm } from "react-hook-form";
import axiosPath from "../../axios";
import "./NewPost.css";

function NewPost() {
  const { register, handleSubmit, reset } = useForm();
  const onSubmit = (data) => {
    console.log(data);
    axiosPath
      .post("", { content: data.content, boast: data.boast })
      .then((res) => console.log("response", res))
      .catch((err) => console.log("err", err));
    reset();
  };
  return (
    <div className="form_contain">
      <form onSubmit={handleSubmit(onSubmit)} className="form_form">
        <h1>New Post Form</h1>
        <label htmlFor="content">Content:</label>
        <input {...register("content", { required: true })} />
        <label htmlFor="boast">Boast or Roast:</label>
        <select {...register("boast", { required: true })}>
          <option value="true">Boast</option>
          <option value="false">Roast</option>
        </select>

        <input type="submit" className="button" />
      </form>
    </div>
  );
}

export default NewPost;
