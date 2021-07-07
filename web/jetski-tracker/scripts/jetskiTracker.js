// https://codepen.io/chingy/pen/Exxvpjo
(function () {
  "use strict";

  const table = document.getElementById("table");
  const tbody = table.querySelector("tbody");

  var currRow = null,
    dragElem = null,
    mouseDownX = 0,
    mouseDownY = 0,
    mouseX = 0,
    mouseY = 0,
    mouseDrag = false;

  function init() {
    bindMouse();
  }

  function bindMouse() {
    document.addEventListener("mousedown", (event) => {
      if (event.button != 0) return true;

      let target = getTargetRow(event.target);
      if (target) {
        currRow = target;
        addDraggableRow(target);
        currRow.classList.add("is-dragging");

        let coords = getMouseCoords(event);
        mouseDownX = coords.x;
        mouseDownY = coords.y;

        mouseDrag = true;
      }
    });

    document.addEventListener("mousemove", (event) => {
      if (!mouseDrag) return;

      let coords = getMouseCoords(event);
      mouseX = coords.x - mouseDownX;
      mouseY = coords.y - mouseDownY;

      moveRow(mouseX, mouseY);
    });

    document.addEventListener("mouseup", (event) => {
      if (!mouseDrag) return;

      currRow.classList.remove("is-dragging");
      table.removeChild(dragElem);

      dragElem = null;
      mouseDrag = false;
    });
  }

  function swapRow(row, index) {
    let currIndex = Array.from(tbody.children).indexOf(currRow),
      row1 = currIndex > index ? currRow : row,
      row2 = currIndex > index ? row : currRow;

    tbody.insertBefore(row1, row2);
  }

  function moveRow(x, y) {
    dragElem.style.transform = "translate3d(" + x + "px, " + y + "px, 0)";

    let dPos = dragElem.getBoundingClientRect(),
      currStartY = dPos.y,
      currEndY = currStartY + dPos.height,
      rows = getRows();

    for (var i = 0; i < rows.length; i++) {
      let rowElem = rows[i],
        rowSize = rowElem.getBoundingClientRect(),
        rowStartY = rowSize.y,
        rowEndY = rowStartY + rowSize.height;

      if (
        currRow !== rowElem &&
        isIntersecting(currStartY, currEndY, rowStartY, rowEndY)
      ) {
        if (Math.abs(currStartY - rowStartY) < rowSize.height / 2)
          swapRow(rowElem, i);
      }
    }
  }

  function addDraggableRow(target) {
    dragElem = target.cloneNode(true);
    dragElem.classList.add("draggable-table__drag");
    dragElem.style.height = getStyle(target, "height");
    dragElem.style.background = getStyle(target, "backgroundColor");
    for (var i = 0; i < target.children.length; i++) {
      let oldTD = target.children[i],
        newTD = dragElem.children[i];
      newTD.style.width = getStyle(oldTD, "width");
      newTD.style.height = getStyle(oldTD, "height");
      newTD.style.padding = getStyle(oldTD, "padding");
      newTD.style.margin = getStyle(oldTD, "margin");
    }

    table.appendChild(dragElem);

    let tPos = target.getBoundingClientRect(),
      dPos = dragElem.getBoundingClientRect();
    dragElem.style.bottom = dPos.y - tPos.y - tPos.height + "px";
    dragElem.style.left = "-1px";

    document.dispatchEvent(
      new MouseEvent("mousemove", {
        view: window,
        cancelable: true,
        bubbles: true,
      })
    );
  }

  function getRows() {
    return table.querySelectorAll("tbody tr");
  }

  function getTargetRow(target) {
    let elemName = target.tagName.toLowerCase();

    if (elemName == "tr") return target;
    if (elemName == "td") return target.closest("tr");
  }

  function getMouseCoords(event) {
    return {
      x: event.clientX,
      y: event.clientY,
    };
  }

  function getStyle(target, styleName) {
    let compStyle = getComputedStyle(target),
      style = compStyle[styleName];

    return style ? style : null;
  }

  function isIntersecting(min0, max0, min1, max1) {
    return (
      Math.max(min0, max0) >= Math.min(min1, max1) &&
      Math.min(min0, max0) <= Math.max(min1, max1)
    );
  }

  init();
})();

// https://mdbootstrap.com/docs/b4/jquery/tables/editable/

const $tableID = $("#table");
const $BTN = $("#export-btn");
const $EXPORT = $("#export");
const newTr = `
<tr class="hide">
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half">
    <span class="table-up"
      ><a href="#!" class="indigo-text"
        ><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a
    ></span>
    <span class="table-down"
      ><a href="#!" class="indigo-text"
        ><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a
    ></span>
  </td>
  <td>
    <span class="table-remove"
      ><button
        type="button"
        class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light"
      >
        Remove
      </button></span
    >
  </td>
</tr>
`;
$(".table-add").on("click", "i", () => {
  const $clone = $tableID
    .find("tbody tr")
    .last()
    .clone(true)
    .removeClass("hide table-line");
  if ($tableID.find("tbody tr").length === 0) {
    $("tbody").append(newTr);
  }
  $tableID.find("table").append($clone);
});
$tableID.on("click", ".table-remove", function () {
  $(this).parents("tr").detach();
});
$tableID.on("click", ".table-up", function () {
  const $row = $(this).parents("tr");
  if ($row.index() === 0) {
    return;
  }
  $row.prev().before($row.get(0));
});
$tableID.on("click", ".table-down", function () {
  const $row = $(this).parents("tr");
  $row.next().after($row.get(0));
});
// A few jQuery helpers for exporting only jQuery.
fn.pop = [].pop;
jQuery.fn.shift = [].shift;
$BTN.on("click", () => {
  const $rows = $tableID.find("tr:not(:hidden)");
  const headers = [];
  const data = [];
  // Get the headers (add special header logic here)
  $($rows.shift())
    .find("th:not(:empty)")
    .each(function () {
      headers.push($(this).text().toLowerCase());
    });
  // Turn all existing rows into a loopable array
  $rows.each(function () {
    const $td = $(this).find("td");
    const h = {};
    // Use the headers from earlier to name our hash keys
    headers.forEach((header, i) => {
      h[header] = $td.eq(i).text();
    });
    data.push(h);
  });
  // Output the result
  $EXPORT.text(JSON.stringify(data));
});
