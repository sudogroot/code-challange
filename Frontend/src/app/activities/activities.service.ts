import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';



const routes = {
  userBooks: () => `/user/books/`
};


@Injectable()
export class ActivitiesService {

  constructor(private httpClient: HttpClient) {
  }

  getUserBooks(page: string = ''): Observable<any> {
    return this.httpClient
      .get(routes.userBooks() + page, {withCredentials: true});
  }

}
