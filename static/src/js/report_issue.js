import { error_message_throw } from "./js modules/tost.js"   // load the toast 
class report_issue {
  constructor() {
    this.geo_btn = document.getElementById("geo-btn");
    this.issue_location = document.getElementById("issue-location");
    this.issue_images = document.getElementById("issue-images");
    this.issue_form = document.getElementById("issue-form"); 
    this.issue_images.addEventListener("change", (e) => {
      this.image_handler(e)
    }
    )
    this.geo_btn.addEventListener("click", (e) => {
      this.geo_btn_handler()
    }
    )
    
    this.issue_form.addEventListener("submit",(e) => {
      e.preventDefault();
      this.form_submit_handler();      
    }
    )


  }








  image_handler(e) {
    const preview_container = document.getElementById("preview-container");
    const upload_prompt = document.getElementById("upload-prompt");
    const files = e.target.files;
    if (files.length > 5) { // check either the bulk image is greater than 5?
      error_message_throw("Image should be less or equal to 5")
      return;
    }
    //if files present then change the icon and acknowledge user their count of images
    if (files) {
      upload_prompt.innerHTML = `
     <i class="fa-solid fa-circle-check text-3xl text-emerald-400"></i> 
                <p class="text-sm font-medium text-emerald-400">${files.length} Photos Selected Successfully</p>
    `
      Array.from(files).forEach((file) => {
        const reader = new FileReader(); //create an reader obj
        reader.onload = function (es) {
          const div = document.createElement("div") // create an wrapper div
          div.className = "relative bg-[#111c2e] p-1 rounded-xl border border-slate-700 overflow-hidden group shadow-md";
          div.innerHTML = `
        <img src='${es.target.result}' alt="" srcset="" class="w-full h-24 object-cover rounded-lg" alt="Upload item" />
        <div class = "absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition duration-150 flex items-center justify-center text-[10px] text-slate-300 font-bold">
        ${(file.size / 1024 / 1024).toFixed(2)} MB
        </div>
        `
          preview_container.appendChild(div);
        }
        reader.readAsDataURL(file);
      }
      )


    }
  }

  // this.geo_btn.addEventListener("click", (e) => {
  // checks for either the browser support the geolocation or not?
  geo_btn_handler() {
    if (!navigator.geolocation) {
      error_message_throw("Geo Location is not supported");
      return
    }
    else {
      navigator.geolocation.getCurrentPosition(
        // if browser support then fetch the latitude and longitude
        (position => {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          this.issue_location.value = `${latitude}, ${longitude}`;
          this.issue_location.readOnly = true;
        }),
        // if user clicks the deny button then run this part!
        (error) => {
          error_message_throw("Permission Denied", "warning")
        }

      )
    }
  }

  async form_submit_handler() {
    const formData = new FormData(this.issue_form);
    const reponse = await fetch("/report_issue",{
      method:"POST",
      body: formData
    })
    const data = await reponse.json()
    console.log(data);
    
  }


}



const s = new report_issue();
