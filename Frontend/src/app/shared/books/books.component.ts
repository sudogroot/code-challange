import {Component, OnInit, Input, EventEmitter, Output} from '@angular/core';
import {BookList} from '@app/models/book';
import {Router} from '@angular/router';


@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.scss']
})
export class BooksComponent implements OnInit {

  @Input() books: BookList;
  @Input() isLoading = false;
  @Output() pageChange = new EventEmitter<string>();


  //  todo add on click return isbn book to view details

  constructor(private router: Router) {
  }

  ngOnInit() {
  }

  navigate(event: any, isbn: string) {
    event.preventDefault();
    this.router.navigate(['../book', isbn]);
  }

  pageBook(page: string) {
    this.pageChange.emit(page);
  }


}
