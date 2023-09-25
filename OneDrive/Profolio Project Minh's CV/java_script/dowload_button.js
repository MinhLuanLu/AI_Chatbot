const downloadCvButton = document.getElementById('downloadCvButton');

    // Define the file URL
    const cvFileUrl = 'minh_luan_lu_cv.pdf'; // Update the file name and path as needed

    // Function to handle the download when the button is clicked
    downloadCvButton.addEventListener('click', () => {
        // Create an anchor element
        const downloadLink = document.createElement('a');
        downloadLink.href = cvFileUrl;
        downloadLink.download = 'files/Minh_CV.pdf'; // Name of the downloaded file

        // Trigger a click event on the anchor element to initiate the download
        downloadLink.click();
    });